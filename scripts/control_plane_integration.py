#!/usr/bin/env python3
"""
Script de integrare și audit pentru control plane-ul extern al proiectului ManualFC.
Aplică directiva Hard Automation Budget și mecanicilor de selecție a taskurilor.
"""

import json
import sys
import io
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

# Set utf-8 output encoding for Windows terminals
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
if sys.stderr.encoding != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

ROOT_DIR = Path(__file__).parent.parent
REGISTRY_PATH = ROOT_DIR / "TASK_REGISTRY.json"
MAX_AUTOMATION_INTERVENTIONS = 2

class ControlPlaneIntegrationError(Exception):
    """Excepție specifică pentru erorile de integrare ale control plane-ului."""
    pass

def load_registry(registry_path: Path = REGISTRY_PATH) -> Dict[str, Any]:
    """Încarcă registrul de taskuri cu verificare fail-closed."""
    if not registry_path.exists():
        raise ControlPlaneIntegrationError(f"Fișierul de registru {registry_path} nu există.")
    try:
        with open(registry_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if "tasks" not in data or not isinstance(data["tasks"], list):
            raise ControlPlaneIntegrationError("Formatul registrului este invalid (lipsește lista 'tasks').")
        return data
    except json.JSONDecodeError as e:
        raise ControlPlaneIntegrationError(f"Registrul JSON este corupt: {e}")

def get_completed_task_ids(registry: Dict[str, Any]) -> set:
    """Returnează setul de ID-uri ale taskurilor finalizate (DONE)."""
    return {
        task["task_id"]
        for task in registry.get("tasks", [])
        if task.get("status") == "DONE"
    }

def get_ready_tasks(registry: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Identifică taskurile în stare READY ale căror dependențe sunt complet închise (DONE).
    """
    completed_ids = get_completed_task_ids(registry)
    ready_tasks = []
    for task in registry.get("tasks", []):
        if task.get("status") == "READY":
            deps = task.get("dependencies", [])
            if all(dep in completed_ids for dep in deps):
                ready_tasks.append(task)
    return ready_tasks

def get_next_ready_task(registry: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Returnează primul task READY de prioritate maximă din registru."""
    ready = get_ready_tasks(registry)
    if not ready:
        return None
    # Sortare după prioritate (CRITICAL -> HIGH -> MEDIUM -> LOW)
    priority_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    ready.sort(key=lambda t: priority_order.get(t.get("priority", "LOW"), 99))
    return ready[0]

def evaluate_automation_budget_gate(gap_status: str, interventions_used: int = 1) -> Dict[str, Any]:
    """
    Evaluează directiva Hard Automation Budget și determină pasul următor.
    """
    gap_status = gap_status.upper()
    if interventions_used > MAX_AUTOMATION_INTERVENTIONS:
        return {
            "status": "BUGET_EXCEEDED",
            "proceed_to_product": True,
            "abandon_automation": True,
            "next_product_task": "TASK-0401",
            "message": "Plafonul de 2 intervenții de automatizare a fost depășit. Trecere directă la produs."
        }
    
    if gap_status == "NONE":
        return {
            "status": "CLEAN_INTEGRATION",
            "proceed_to_product": True,
            "abandon_automation": False,
            "next_product_task": "TASK-0401",
            "message": "Integrare curată fără gap (NONE). Trecere directă la dezvoltarea produsului TASK-0401."
        }
    elif gap_status == "SMALL_ADAPTER":
        return {
            "status": "SINGLE_ADAPTER_ALLOWED",
            "proceed_to_product": False,
            "abandon_automation": False,
            "allowed_extra_tasks": 1,
            "message": "Gap mic (SMALL_ADAPTER). Este permis UN singur task suplimentar pentru adaptorul minim."
        }
    elif gap_status in ("MODERATE_GAP", "MAJOR_REWORK"):
        return {
            "status": "AUTOMATION_ABANDONED",
            "proceed_to_product": True,
            "abandon_automation": True,
            "next_product_task": "TASK-0401",
            "message": f"Gap excesiv ({gap_status}). Se abandonează extinderea automatizării și se trece la TASK-0401."
        }
    else:
        raise ControlPlaneIntegrationError(f"Stare de gap necunoscută: {gap_status}")

def verify_task_outputs(task_id: str, registry: Dict[str, Any], base_dir: Path = ROOT_DIR) -> Tuple[bool, List[str]]:
    """Verifică dacă toate outputurile declarate pentru un task există pe disc."""
    tasks_dict = {t["task_id"]: t for t in registry.get("tasks", [])}
    if task_id not in tasks_dict:
        return False, [f"Task-ul {task_id} nu există în registru."]
    
    task = tasks_dict[task_id]
    outputs = task.get("outputs", [])
    missing = []
    for rel_path in outputs:
        full_path = base_dir / rel_path
        if not full_path.exists():
            missing.append(rel_path)
    return len(missing) == 0, missing

def audit_control_plane_status() -> Dict[str, Any]:
    """Efectuează auditul complet al stării integrării control plane-ului."""
    registry = load_registry()
    next_task = get_next_ready_task(registry)
    completed_ids = get_completed_task_ids(registry)
    gate_result = evaluate_automation_budget_gate("NONE", interventions_used=1)
    
    return {
        "total_tasks": len(registry.get("tasks", [])),
        "completed_tasks": len(completed_ids),
        "next_ready_task": next_task["task_id"] if next_task else None,
        "next_ready_title": next_task["title"] if next_task else None,
        "automation_budget_used": "1/2",
        "gate_status": gate_result["status"],
        "next_product_task": gate_result["next_product_task"]
    }

def main():
    try:
        registry = load_registry()
        ready_task = get_next_ready_task(registry)
        print("=== Audit Control Plane ManualFC ===")
        print(f"Total taskuri in registru: {len(registry.get('tasks', []))}")
        print(f"Taskuri finalizate (DONE): {len(get_completed_task_ids(registry))}")
        if ready_task:
            print(f"Urmatorul task READY: {ready_task['task_id']} -- {ready_task['title']}")
        else:
            print("Nu exista taskuri READY disponibile.")
        
        gate = evaluate_automation_budget_gate("NONE", interventions_used=1)
        print(f"Status Hard Automation Budget Gate: {gate['message']}")
        sys.exit(0)
    except Exception as e:
        print(f"EROARE Control Plane Integration: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
