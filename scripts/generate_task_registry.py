#!/usr/bin/env python3
"""Generează determinist registrul granular al proiectului Manual U11."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "TASK_REGISTRY.json"
TASKS: list[dict] = []


def add(
    task_id: str,
    title: str,
    phase: str,
    dependencies: list[str],
    outputs: list[str],
    acceptance: list[str],
    *,
    priority: str = "HIGH",
    volume: str | None = None,
    units: int = 3,
    status: str = "PENDING",
    validations: list[str] | None = None,
    migration_disposition: str = "KEEP_WITH_WEB_OUTPUT",
) -> None:
    TASKS.append({
        "task_id": task_id,
        "title": title,
        "phase": phase,
        "volume": volume,
        "status": status,
        "priority": priority,
        "dependencies": dependencies,
        "outputs": outputs,
        "acceptance_criteria": acceptance,
        "validation_commands": validations or ["python scripts/validate_project.py"],
        "weight_units": units,
        "attempts": 0,
        "max_attempts": 4,
        "last_error": None,
        "created_at": "2026-07-30",
        "started_at": None,
        "completed_at": None,
        "migration_disposition": migration_disposition,
    })


REPORT = lambda tid: f"reports/task-reports/{tid}.md"
SCHEMA_OK = ["Outputurile declarate există.", "Validările declarate ies cu cod 0.", "Raportul conține dovezi și limite."]
CHAPTER_OK = SCHEMA_OK + [
    "Livrabilul este un capitol publicabil, nu o schiță.",
    "Afirmațiile factuale importante sunt legate de registrul de cercetare.",
    "Mesajele către copil au fundamentarea completă și tratează categoria 2015–2016 unitar.",
    "Auditul factual, pedagogic și editorial este înregistrat separat."
]
BATCH_EX_OK = SCHEMA_OK + [
    "Lotul conține exact 4 exerciții validate contra schemei.",
    "Fiecare exercițiu are maximum trei comportamente, dimensiuni justificate, siguranță, diagramă și echivalent PDF.",
    "Fiecare mesaj, regulă, întrebare și feedback către copil are fundamentare completă.",
    "Fezabilitatea, timpul activ și transferul în meci sunt verificate."
]
BATCH_SES_OK = SCHEMA_OK + [
    "Lotul conține exact 2 ședințe validate contra schemei.",
    "Fiecare ședință justifică ordinea, durata, tranzițiile și timpul activ.",
    "Jocul final verifică transferul cu constrângerile artificiale eliminate.",
    "Harta suprafeței și adaptările pentru efective diferite sunt validate."
]

# PHASE-00 — bootstrap
add("TASK-0001", "Inițializare, arhitectură și registru executabil", "PHASE-00", [],
    ["plans/TASK-0001-initializare-arhitectura.md", "docs/architecture/ADR-0001-STACK-SI-FLUX-DATE.md",
     "docs/architecture/DATA_AND_CITATION_SYSTEM.md", "docs/architecture/VISUAL_SYSTEM.md",
     "docs/architecture/BUILD_AND_TEST_STRATEGY.md", "config/project.json", "config/visual-tokens.json",
     "research/sources.json", "research/claims.json", "research/citations.json", REPORT("TASK-0001")],
    SCHEMA_OK + ["Registrul este granular, aciclic și are ponderi cu suma 100.", "Structura persistentă există fără conținut demonstrativ."],
    priority="CRITICAL", units=4, status="DONE",
    validations=["python scripts/generate_task_registry.py --check", "python scripts/validate_project.py", "python -m unittest discover -s tests -p \"test_*.py\""])
add("TASK-0002", "Inițializarea repository-ului Git și fixarea baseline-ului inițial", "PHASE-00", ["TASK-0001"],
    [".gitignore", ".gitattributes", REPORT("TASK-0002")],
    SCHEMA_OK + ["Repository-ul Git este inițializat numai cu autorizare.", "Politica pentru fișiere generate și finale este documentată."],
    priority="MEDIUM", units=1, status="DONE")
add("TASK-0003", "Pivotul produsului către platformă web pedagogică și migrarea roadmapului", "PHASE-00", ["TASK-0002", "TASK-0104"],
    ["PRODUCT_VISION.md", "PRODUCT_REQUIREMENTS.md", "TARGET_USERS.md", "INFORMATION_ARCHITECTURE.md",
     "CONTENT_STRATEGY.md", "PEDAGOGICAL_PRODUCT_PRINCIPLES.md", "MULTIMEDIA_AND_TACTICAL_VISUALS.md",
     "PILOT_AND_FEEDBACK_STRATEGY.md", "COMMERCIALIZATION_ROADMAP.md", "MULTI_AGE_EXPANSION_ARCHITECTURE.md",
     "ROADMAP_MIGRATION_REPORT.md", "plans/TASK-0003-pivot-platforma-web.md", REPORT("TASK-0003")],
    SCHEMA_OK + ["Platforma web este livrabilul principal.", "Toate taskurile au o dispoziție de migrare.",
                 "Progresul taskurilor DONE este păstrat."], priority="CRITICAL", units=5, status="DONE",
    migration_disposition="KEEP_UNCHANGED")
add("TASK-0004", "TASK-0004 — Integrarea ManualFC cu control plane-ul autonom existent", "PHASE-00", ["TASK-0003"],
    ["docs/architecture/EXTERNAL_CONTROL_PLANE_INTEGRATION.md", "scripts/control_plane_integration.py", "tests/test_control_plane_integration.py", REPORT("TASK-0004")],
    SCHEMA_OK + ["Contractul descrie reutilizarea unui control plane extern existent pentru selecția taskurilor READY.",
                 "Control plane-ul extern asigură ordine pe baza dependențelor DONE fără a construi un orchestrator autonom intern.",
                 "Nu extinde autorizarea și păstrează un singur task principal."],
    priority="CRITICAL", units=4, status="DONE", migration_disposition="MOVE_EARLIER")

# PHASE-01 — research contracts and transversal research
add("TASK-0101", "Validator JSON Schema și referințe încrucișate", "PHASE-01", ["TASK-0001"],
    ["plans/TASK-0101-validator-date-referinte.md", "scripts/validate_content.py",
     "scripts/validation/codes.py", "tests/test_content_validator.py",
     "tests/fixtures/validation/cases.json", "docs/architecture/VALIDATION_SYSTEM.md",
     "requirements-dev.txt", REPORT("TASK-0101")],
    SCHEMA_OK + ["Toate registrele și entitățile sunt validate contra schemei.", "ID-urile orfane și duplicate blochează validarea."], units=3, status="READY")
add("TASK-0102", "Protocol operațional de căutare, arhivare și versiuni", "PHASE-01", ["TASK-0001"],
    ["plans/TASK-0102-protocol-cercetare-arhivare-versionare.md",
     "config/research-taxonomy.json", "docs/research/RESEARCH_PROTOCOL.md",
     "docs/research/ARCHIVING_POLICY.md", "docs/research/VERSIONING_POLICY.md",
     "docs/research/FRESHNESS_POLICY.md", "docs/research/VISUAL_RIGHTS_POLICY.md",
     "docs/research/REGISTRY_GUIDE.md", "docs/research/CONFLICTING_SOURCES.md",
     "docs/research/EXACT_CITATION_GUIDE.md", "docs/research/TOOLS.md",
     "scripts/research_tool.py", "scripts/migrate_research_v1_to_v2.py",
     "schemas/research-question.schema.json", "schemas/search-log.schema.json",
     "schemas/archive-manifest.schema.json", "research/questions.json",
     "research/search-logs.jsonl", "research/archive-manifests.json",
     "tests/test_research_protocol.py", REPORT("TASK-0102")],
    SCHEMA_OK + ["Protocolul diferențiază sursa primară, versiunea, data accesării și indisponibilitatea.", "Nu conține surse inventate."],
    units=2, status="DONE",
    validations=["python scripts/validate_content.py", "python scripts/validate_content.py --strict",
                 "python scripts/validate_project.py", "python -m unittest discover -s tests -v",
                 "git diff --check"])
research_topics = [
    ("0103", "Regulamente, formate și dimensiuni U11 actuale", "regulations-u11"),
    ("0104", "Safeguarding și protecția copilului", "safeguarding"),
    ("0105", "Dezvoltare cognitivă, psihologică și socială la 10–11 ani", "development"),
    ("0106", "Învățare motrică, feedback și autonomie", "motor-learning"),
    ("0107", "Jocuri reduse, constrângeri și reprezentativitate", "small-sided-games"),
    ("0108", "Încărcare, recuperare, siguranță și maturizare", "load-safety"),
    ("0109", "Relația antrenor–părinte–copil", "coach-parent-child"),
]
for code, title, slug in research_topics:
    tid = f"TASK-{code}"
    add(tid, f"Dosar de cercetare — {title}", "PHASE-01", ["TASK-0101", "TASK-0102"],
        [f"research/dossiers/{slug}.md", REPORT(tid)],
        SCHEMA_OK + ["Sursele primare și instituționale sunt prioritizate.", "Afirmațiile, limitele și aplicabilitatea la categoria unică 10–11 ani sunt înregistrate."], units=4)
task_0103 = next(task for task in TASKS if task["task_id"] == "TASK-0103")
task_0103["outputs"] = [
    "plans/TASK-0103-dosar-regulamente-u11.md",
    "research/dossiers/regulations-u11.md",
    "research/dossiers/ajf-satu-mare-u11.md",
    "research/dossiers/missing-documents.md",
    "research/dossiers/ajf-request-template.md",
    "research/dossiers/regulations-recheck-policy.md",
    "research/audits/TASK-0103-factual-temporal-audit.md",
    "data/regulations/u11-rules.json",
    "data/regulations/u11-conflicts.json",
    "data/regulations/u11-space-per-player.json",
    REPORT("TASK-0103"),
]
task_0103["validation_commands"] = [
    "python scripts/validate_regulations.py",
    "python -m unittest tests.test_regulations -v",
    "python scripts/validate_content.py",
    "python scripts/validate_content.py --strict",
    "python scripts/validate_project.py",
    "python scripts/generate_task_registry.py --check",
    "git diff --check",
]
task_0104 = next(task for task in TASKS if task["task_id"] == "TASK-0104")
task_0104["outputs"] = [
    "plans/TASK-0104-safeguarding-protectia-copilului.md",
    "schemas/safeguarding.schema.json",
    "data/safeguarding/canonical.json",
    "research/dossiers/safeguarding.md",
    "research/dossiers/safeguarding-matrices.md",
    "research/dossiers/safeguarding-models.md",
    "research/dossiers/safeguarding-codes.md",
    "research/dossiers/safeguarding-digital-visual.md",
    "research/dossiers/safeguarding-contacts.md",
    "research/dossiers/safeguarding-scripts.md",
    "research/dossiers/safeguarding-recheck-policy.md",
    "research/audits/TASK-0104-legal-audit.md",
    "research/audits/TASK-0104-practical-language-audit.md",
    "assets/safeguarding/disclosure-response.svg",
    "assets/safeguarding/escalation.svg",
    "assets/safeguarding/trusted-adults.svg",
    "scripts/validate_safeguarding.py",
    "tests/test_safeguarding.py",
    REPORT("TASK-0104"),
]
task_0104["validation_commands"] = [
    "python scripts/validate_safeguarding.py",
    "python -m unittest tests.test_safeguarding -v",
    "python scripts/validate_content.py",
    "python scripts/validate_content.py --strict",
    "python scripts/validate_project.py",
    "python scripts/generate_task_registry.py --check",
    "git diff --check",
]

# Pivot web: fundația și prototipul vertical preced producția editorială.
for task in TASKS:
    if task["task_id"] in {"TASK-0105", "TASK-0106", "TASK-0107", "TASK-0108", "TASK-0109"}:
        task["dependencies"] = ["TASK-0101", "TASK-0102", "TASK-0415"]
        task["migration_disposition"] = "MOVE_LATER"
        task["acceptance_criteria"].append("Rezultatele alimentează pagini web aprofundate și rapide, fără a combina auditul științific cu pilotul de teren.")

add("TASK-0410", "Specificația prototipului — Sprijinul și unghiul de pasă", "PHASE-04", ["TASK-0304", "TASK-0407"],
    ["docs/prototype/SUPPORT_PASSING_ANGLE_SPEC.md", REPORT("TASK-0410")],
    SCHEMA_OK + ["Specificația acoperă lecția, 5 exerciții, 2 ședințe, evaluarea, mobilul, PDF-ul și feedbackul."], units=3,
    migration_disposition="MOVE_EARLIER")
add("TASK-0411", "Producția prototipului — Sprijinul și unghiul de pasă", "PHASE-04", ["TASK-0410"],
    ["app/src/pages/prototip/sprijin-unghi-pasa.astro", "data/prototypes/support-passing-angle.json", REPORT("TASK-0411")],
    SCHEMA_OK + ["Prototipul include diagramă statică, animație, fallback PDF, 5 exerciții și 2 ședințe."], units=6,
    migration_disposition="MOVE_EARLIER")
add("TASK-0412", "Audit independent al prototipului vertical", "PHASE-04", ["TASK-0411"],
    ["reports/prototype/support-passing-angle-audit.md", REPORT("TASK-0412")],
    SCHEMA_OK + ["Auditul acoperă factual, pedagogic, editorial, vizual, mobil și accesibilitate."], units=3,
    migration_disposition="MOVE_EARLIER")
add("TASK-0413", "Testarea pe teren a prototipului", "PHASE-04", ["TASK-0412"],
    ["reports/pilot/support-passing-angle-field-test.md", REPORT("TASK-0413")],
    SCHEMA_OK + ["Nu se stochează date personale identificabile despre copii.", "Feedbackul practic rămâne separat de dovezile științifice."], units=3,
    migration_disposition="MOVE_EARLIER")
add("TASK-0414", "Repararea prototipului după audit și pilot", "PHASE-04", ["TASK-0412", "TASK-0413"],
    ["reports/prototype/support-passing-angle-repair.md", REPORT("TASK-0414")], SCHEMA_OK, units=3,
    migration_disposition="MOVE_EARLIER")
add("TASK-0415", "Blocarea șablonului canonic de producție", "PHASE-04", ["TASK-0414"],
    ["templates/canonical-page-contract.md", "reports/prototype/canonical-template-approval.md", REPORT("TASK-0415")],
    SCHEMA_OK + ["Șablonul blochează cele 18 întrebări, multimedia, accesibilitatea și fallbackul PDF."], units=3,
    migration_disposition="MOVE_EARLIER")
add("TASK-0416", "Versiunea pilot a platformei U11", "PHASE-04", ["TASK-0415", "TASK-1604"],
    ["reports/pilot/u11-platform-pilot.md", REPORT("TASK-0416")], SCHEMA_OK, units=4,
    migration_disposition="MOVE_LATER")
add("TASK-0417", "Validarea comercială fără monetizare implementată", "PHASE-04", ["TASK-0416"],
    ["reports/commercial/validation.md", REPORT("TASK-0417")],
    SCHEMA_OK + ["Sunt evaluate utilizarea, revenirea, valoarea și disponibilitatea de plată fără paywall sau date personale."], units=3,
    migration_disposition="MOVE_LATER")
add("TASK-0418", "Decizie de extindere multi-age după validare", "PHASE-04", ["TASK-0417", "TASK-2103"],
    ["reports/product/multi-age-expansion-decision.md", REPORT("TASK-0418")],
    SCHEMA_OK + ["Nu produce conținut pentru alte vârste; decide numai ordinea viitoare."], units=2,
    migration_disposition="DEFER_TO_MULTI_AGE")

# Ordinea canonică de după orchestrator.
web_sequence = {
    "TASK-0401": (["TASK-0004"], "Fundația arhitecturii site-ului Astro și TypeScript strict"),
    "TASK-0302": (["TASK-0401"], "Design system web, editorial, print și accesibilitate"),
    "TASK-0201": (["TASK-0302"], "Taxonomie și arhitectură pentru conținut și pagini"),
    "TASK-0402": (["TASK-0201"], "Sistem tipizat de conținut, pagini și relații"),
    "TASK-0303": (["TASK-0402"], "Specificația motorului de diagrame SVG"),
    "TASK-0403": (["TASK-0303"], "Motor SVG și renderer static"),
    "TASK-0304": (["TASK-0403"], "Specificația motorului de animații și fallback PDF"),
    "TASK-0404": (["TASK-0304"], "Motor de animație tactică accesibil"),
    "TASK-0405": (["TASK-0404"], "Shell web cu cele două moduri, navigație, căutare și offline"),
    "TASK-0407": (["TASK-0405"], "Harness Playwright pentru browser, mobil, accesibilitate și vizual"),
}
for task in TASKS:
    if task["task_id"] in web_sequence:
        task["dependencies"], task["title"] = web_sequence[task["task_id"]]
        task["migration_disposition"] = "MOVE_EARLIER"
        task["acceptance_criteria"].extend(["Accesibilitatea web este obligatorie.", "Orice situație dinamică are fallback PDF."])
    if task["title"].startswith("Capitol —"):
        task["migration_disposition"] = "SPLIT"
        task["acceptance_criteria"].append("Producția, auditul pedagogic și auditul editorial rămân verificări distincte.")
    if task["task_id"] in {"TASK-1401", "TASK-1402", "TASK-1403", "TASK-1404"}:
        task["migration_disposition"] = "REPLACE"
    if task["task_id"].startswith("TASK-17"):
        task["migration_disposition"] = "MOVE_LATER"
add("TASK-0110", "Audit transversal al afirmațiilor cu impact ridicat", "PHASE-01",
    [f"TASK-{code}" for code, _, _ in research_topics],
    ["reports/research/high-impact-claims-audit.md", REPORT("TASK-0110")],
    SCHEMA_OK + ["Sunt verificate toate afirmațiile de siguranță, dezvoltare, reguli și eficiență metodologică.", "Problemele reale deschid taskuri de reparare."], units=3)
add("TASK-0111", "Reverificare regulamente U11 2026–2027", "PHASE-01", ["TASK-0103"],
    ["research/dossiers/regulations-u11-recheck.md", REPORT("TASK-0111")],
    SCHEMA_OK + ["Locațiile oficiale FRF și AJF Satu Mare sunt reverificate.",
                 "Orice document nou înlocuiește explicit statutul provizoriu sau necunoscut."],
    units=1, status="READY")

# PHASE-02/03/04 — canonical systems
systems = [
    ("0201", "Taxonomie editorială, volume, capitole și metadate", "docs/architecture/CONTENT_MODEL.md", ["TASK-0001"]),
    ("0202", "Schema canonică a capitolului și a referințelor", "schemas/chapter.schema.json", ["TASK-0201", "TASK-0101"]),
    ("0203", "Glosar canonic și reguli terminologice", "data/glossary.json", ["TASK-0201", "TASK-0103"]),
    ("0204", "Model canonic pentru evaluări și rubrici", "schemas/assessment.schema.json", ["TASK-0201", "TASK-0105"]),
    ("0205", "Model canonic pentru scripturi și studii de caz", "schemas/communication-script.schema.json", ["TASK-0201", "TASK-0105", "TASK-0109"]),
    ("0206", "Model canonic pentru planuri anuale și microcicluri", "schemas/season-plan.schema.json", ["TASK-0201", "TASK-0108"]),
    ("0301", "Ghid operațional pentru fundamentarea mesajelor", "docs/MESSAGE_FOUNDATION_GUIDE.md", ["TASK-0105", "TASK-0106"]),
    ("0302", "Design system editorial, print și accesibilitate", "docs/architecture/DESIGN_SYSTEM.md", ["TASK-0001"]),
    ("0303", "Specificația generatorului de diagrame SVG", "docs/architecture/DIAGRAM_ENGINE.md", ["TASK-0302"]),
    ("0304", "Specificația animațiilor și cadrelor PDF", "docs/architecture/ANIMATION_ENGINE.md", ["TASK-0303"]),
    ("0305", "Șabloane editoriale fără conținut demonstrativ", "templates/README.md", ["TASK-0202", "TASK-0301"]),
    ("0306", "Rubrici automate pentru porțile pedagogice și editoriale", "config/quality-rubrics.json", ["TASK-0301", "TASK-0204"]),
    ("0401", "Bootstrap Astro și TypeScript strict", "package.json", ["TASK-0101", "TASK-0202", "TASK-0302"]),
    ("0402", "Loader tipizat pentru conținut și date", "app/src/lib/content-loader.ts", ["TASK-0401", "TASK-0202"]),
    ("0403", "Motor SVG și renderer static", "app/src/lib/diagram-renderer.ts", ["TASK-0401", "TASK-0303"]),
    ("0404", "Player de animație accesibil", "app/src/components/TacticalPlayer.tsx", ["TASK-0401", "TASK-0304"]),
    ("0405", "Shell web, navigație, căutare și offline", "app/src/layouts/ManualLayout.astro", ["TASK-0402"]),
    ("0406", "Pipeline print și prototip PDF reprezentativ", "print/print.css", ["TASK-0402", "TASK-0302"]),
    ("0407", "Harness Playwright pentru browser, accesibilitate și vizual", "playwright.config.ts", ["TASK-0405", "TASK-0406"]),
    ("0408", "Auditul prototipului tehnic și vizual", "reports/audits/prototype-audit.md", ["TASK-0403", "TASK-0404", "TASK-0405", "TASK-0406", "TASK-0407"]),
]
for code, title, output, deps in systems:
    tid = f"TASK-{code}"
    add(tid, title, f"PHASE-{code[:2]}", deps, [output, REPORT(tid)],
        SCHEMA_OK + ["Contractul sau modulul este documentat și testat la nivelul adecvat.", "Nu introduce conținut demonstrativ în produs."], units=3)

# Volumes I–V: one chapter per task, followed by independent audit and repair gate.
volume_specs = {
    "05": ("VOLUME-01", [
        "Profilul variabil al copilului de 10–11 ani", "Percepție, orientare și atenție în joc",
        "Decizie, execuție și valoarea greșelii", "Motivație, autonomie și încredere",
        "Cooperare, apartenență și diferențiere individuală"]),
    "06": ("VOLUME-02", [
        "Jocul ca sistem de probleme", "Principii în posesie: spațiu și unghiuri",
        "Principii în posesie: progresie și sprijin", "Principii fără minge: protejarea centrului",
        "Principii fără minge: presiune și acoperire", "Tranziția la pierderea mingii",
        "Tranziția la câștigarea mingii", "Superioritate, egalitate și inferioritate numerică"]),
    "07": ("VOLUME-03", [
        "Limbaj scurt și informație relevantă", "Întrebări, feedback și verificarea înțelegerii",
        "Emoții, greșeală și climat de siguranță", "Disciplina fără umilire",
        "Comunicarea în meci și evitarea joystick coaching", "Conversații individuale și echitate"]),
    "08": ("VOLUME-04", [
        "Proiectarea unei situații reprezentative", "Constrângeri: alegere, dozare și eliminare",
        "Progresii și regresii fără pierderea intenției", "Observare și criterii de intervenție",
        "Organizare, rotații, timp activ și siguranță", "Transferul și reflecția după joc"]),
    "09": ("VOLUME-05", [
        "Rezultate de învățare și traseul anual", "Plan anual cu două antrenamente și meci",
        "Plan anual cu trei antrenamente și meci", "Microcicluri și adaptarea încărcării",
        "Rotația rolurilor și diferențierea individuală", "Monitorizare, revizie și continuitate"]),
}
volume_last: dict[str, str] = {}
for phase, (volume, chapters) in volume_specs.items():
    base = int(phase) * 100
    prereq = {"05": ["TASK-0202", "TASK-0111"], "06": ["TASK-0507"], "07": ["TASK-0507"],
              "08": ["TASK-0708"], "09": ["TASK-0808", "TASK-0206"]}[phase]
    chapter_ids = []
    for index, title in enumerate(chapters, 1):
        tid = f"TASK-{base + index:04d}"
        chapter_ids.append(tid)
        add(tid, f"Capitol — {title}", f"PHASE-{phase}", prereq,
            [f"content/volume-{int(phase)-4:02d}/chapter-{index:02d}.mdx", REPORT(tid)],
            CHAPTER_OK, volume=volume, units=5)
    audit = f"TASK-{base + len(chapters) + 1:04d}"
    repair = f"TASK-{base + len(chapters) + 2:04d}"
    add(audit, f"Audit independent {volume}", f"PHASE-{phase}", chapter_ids,
        [f"reports/audits/{volume.lower()}-audit.md", REPORT(audit)],
        SCHEMA_OK + ["Auditul separă factualitatea, pedagogia, structura, limba, vizualul și integrarea.", "Defectele sunt clasificate și au task de reparare."],
        volume=volume, units=3)
    add(repair, f"Reparare și aprobare {volume}", f"PHASE-{phase}", [audit],
        [f"reports/audits/{volume.lower()}-approval.md", REPORT(repair)],
        SCHEMA_OK + ["Toate defectele critice și mari sunt închise sau taskul rămâne incomplet.", "Volumul este integrabil fără contradicții cunoscute."],
        volume=volume, units=3)
    volume_last[phase] = repair

# Forensic remediation: TASK-0709/TASK-0809 reopen the chapters whose sole primary
# source was found fabricated or mismatched by the post-TASK-0808 forensic audit
# (reports/audits/POST_TASK0608_FORENSIC_AUDIT.md, DEC-0040). CH-0306 and CH-0401 are
# excluded — their sources (SRC-0057, SRC-0058) were independently verified as correct.
add("TASK-0709", "Remediere cercetare și conținut VOLUME-03 (CH-0301-CH-0305)", "PHASE-07", ["TASK-0708"],
    ["research/sources.json", "research/claims.json", "research/citations.json",
     "content/volume-03/chapter-01.mdx", "content/volume-03/chapter-02.mdx", "content/volume-03/chapter-03.mdx",
     "content/volume-03/chapter-04.mdx", "content/volume-03/chapter-05.mdx", REPORT("TASK-0709")],
    SCHEMA_OK + [
        "Fiecare sursă folosită este verificată extern (DOI rezolvat la doi.org/CrossRef, titlu și populație confirmate) înainte de a fi citată.",
        "Cele trei numere exacte identificate ca nesusținute (regula celor 15 secunde, orice prag temporal similar) sunt fie eliminate, fie etichetate explicit MANUALFC_HEURISTIC.",
        "Claims marcate CONTESTED (CLM-0054..CLM-0057) sunt înlocuite cu claims noi, verificate, sau retrogradate onest la PRACTICE_ONLY cu sursă reală pentru context.",
        "CH-0306 nu este atins (sursa lui este validă)."
    ],
    volume="VOLUME-03", units=8, status="READY")
add("TASK-0710", "Audit independent VOLUME-03 (post-remediere TASK-0709)", "PHASE-07", ["TASK-0709"],
    ["reports/audits/volume-03-forensic-remediation-audit.md", REPORT("TASK-0710")],
    SCHEMA_OK + [
        "Auditul e realizat separat de reparație — nu combină verificarea cu munca de corectare (lecția din TASK-0807/DEC-0040).",
        "Sursele-cheie de înlocuire sunt re-verificate independent bibliografic (titlu, autori, an), nu doar prin DOI care rezolvă.",
        "Toate cele 6 capitole (CH-0301-CH-0306) sunt evaluate: calitatea cercetării, calibrarea claim-urilor, nivelul epistemic, aplicabilitatea U11, traducerea practică, limbajul pentru copii, integritatea numerelor exacte, duplicarea cu alte volume, siguranța și relevanța pentru fotbal.",
        "Verdictul este binar: PASS_FIELD_REVIEW_READY sau REPAIR_REQUIRED — fără stare parțială."
    ],
    volume="VOLUME-03", units=3, status="READY")
add("TASK-0809", "Remediere cercetare și conținut VOLUME-04 (CH-0402-CH-0406)", "PHASE-08", ["TASK-0808"],
    ["research/sources.json", "research/claims.json", "research/citations.json",
     "content/volume-04/chapter-02.mdx", "content/volume-04/chapter-03.mdx", "content/volume-04/chapter-04.mdx",
     "content/volume-04/chapter-05.mdx", "content/volume-04/chapter-06.mdx", REPORT("TASK-0809")],
    SCHEMA_OK + [
        "Fiecare sursă folosită este verificată extern (DOI rezolvat la doi.org/CrossRef, titlu și populație confirmate) înainte de a fi citată.",
        "Cele două numere exacte identificate ca nesusținute (timp activ peste 70%, debriefing de 3-5 minute) sunt fie eliminate, fie etichetate explicit MANUALFC_HEURISTIC.",
        "Claims marcate CONTESTED (CLM-0060..CLM-0064) sunt înlocuite cu claims noi, verificate, sau retrogradate onest la PRACTICE_ONLY cu sursă reală pentru context.",
        "CH-0401 nu este atins (sursa lui este validă)."
    ],
    volume="VOLUME-04", units=8, status="READY")
add("TASK-0810", "Audit independent VOLUME-04 (post-remediere TASK-0809)", "PHASE-08", ["TASK-0809"],
    ["reports/audits/volume-04-forensic-remediation-audit.md", REPORT("TASK-0810")],
    SCHEMA_OK + [
        "Auditul e realizat separat de reparație — nu combină verificarea cu munca de corectare (lecția din TASK-0807/DEC-0040).",
        "Sursele-cheie de înlocuire sunt re-verificate independent bibliografic (titlu, autori, an), nu doar prin DOI care rezolvă.",
        "Toate cele 6 capitole (CH-0401-CH-0406) sunt evaluate: calitatea cercetării, calibrarea claim-urilor, nivelul epistemic, aplicabilitatea U11, traducerea practică, limbajul pentru copii, integritatea numerelor exacte, duplicarea cu alte volume, siguranța și relevanța pentru fotbal.",
        "Verdictul este binar: PASS_FIELD_REVIEW_READY sau REPAIR_REQUIRED — fără stare parțială."
    ],
    volume="VOLUME-04", units=3, status="READY")

# Communication scripts and case studies are separate, reviewable batches.
script_ids = []
for i in range(10):
    tid = f"TASK-{750 + i:04d}"
    script_ids.append(tid)
    add(tid, f"Lot scripturi de comunicare {i + 1} — 5 scripturi", "PHASE-07", [volume_last["07"]],
        [f"data/communication-scripts/batch-{i + 1:02d}.json", REPORT(tid)],
        SCHEMA_OK + ["Lotul conține exact 5 scripturi.", "Fiecare replică are fundamentare, risc, verificare și alternativă."],
        volume="VOLUME-03", units=2)
case_ids = []
for i in range(5):
    tid = f"TASK-{770 + i:04d}"
    case_ids.append(tid)
    add(tid, f"Lot studii de caz {i + 1} — 3 scenarii", "PHASE-07", [volume_last["07"]],
        [f"data/case-studies/batch-{i + 1:02d}.json", REPORT(tid)],
        SCHEMA_OK + ["Lotul conține exact 3 scenarii etichetate explicit drept didactice.", "Scenariile nu pretind întâmplări reale și includ alternative argumentate."],
        volume="VOLUME-03", units=2)
add("TASK-0780", "Auditul bibliotecii de comunicare și al studiilor de caz", "PHASE-07", script_ids + case_ids,
    ["reports/audits/communication-library-audit.md", REPORT("TASK-0780")],
    SCHEMA_OK + ["Sunt confirmate minimum 50 de scripturi și 15 studii de caz.", "Fundamentarea și diversitatea situațiilor sunt auditate."],
    volume="VOLUME-03", units=3)

# Exercise library: 15 batches × 4 = 60.
exercise_batches = []
for i in range(15):
    tid = f"TASK-{1001 + i:04d}"
    exercise_batches.append(tid)
    add(tid, f"Lot exerciții {i + 1} — 4 exerciții", "PHASE-10",
        [volume_last["06"], volume_last["08"], volume_last["09"], "TASK-0408"],
        [f"data/exercises/batch-{i + 1:02d}.json", f"assets/manifests/exercise-batch-{i + 1:02d}.json", REPORT(tid)],
        BATCH_EX_OK, volume="VOLUME-06", units=6)
exercise_audits = []
for index, group in enumerate((exercise_batches[:5], exercise_batches[5:10], exercise_batches[10:]), 1):
    tid = f"TASK-{1020 + index:04d}"
    exercise_audits.append(tid)
    add(tid, f"Audit independent exerciții — loturile {(index-1)*5+1}–{index*5}", "PHASE-10", group,
        [f"reports/audits/exercises-{index:02d}.md", REPORT(tid)],
        SCHEMA_OK + ["Datele, diagramele și descrierile sunt coerente.", "Fezabilitatea și fundamentarea sunt verificate independent."],
        volume="VOLUME-06", units=3)
add("TASK-1024", "Integrarea și aprobarea bibliotecii de 60 de exerciții", "PHASE-10", exercise_audits,
    ["content/volume-06/index.mdx", "reports/audits/exercise-library-approval.md", REPORT("TASK-1024")],
    SCHEMA_OK + ["Există minimum 60 de exerciții unice și validate.", "Acoperirea temelor și progresia sunt documentate."],
    volume="VOLUME-06", units=4)

# Session library: 18 batches × 2 = 36.
session_batches = []
for i in range(18):
    tid = f"TASK-{1101 + i:04d}"
    session_batches.append(tid)
    add(tid, f"Lot ședințe {i + 1} — 2 ședințe", "PHASE-11", ["TASK-1024", volume_last["09"]],
        [f"data/sessions/batch-{i + 1:02d}.json", f"assets/manifests/session-batch-{i + 1:02d}.json", REPORT(tid)],
        BATCH_SES_OK, volume="VOLUME-07", units=6)
session_audits = []
for index, group in enumerate((session_batches[:6], session_batches[6:12], session_batches[12:]), 1):
    tid = f"TASK-{1120 + index:04d}"
    session_audits.append(tid)
    add(tid, f"Audit independent ședințe — loturile {(index-1)*6+1}–{index*6}", "PHASE-11", group,
        [f"reports/audits/sessions-{index:02d}.md", REPORT(tid)],
        SCHEMA_OK + ["Ordinea, logistica, încărcarea și transferul sunt verificate.", "Referințele către exerciții sunt valide."],
        volume="VOLUME-07", units=3)
add("TASK-1124", "Integrarea și aprobarea bibliotecii de 36 de ședințe", "PHASE-11", session_audits,
    ["content/volume-07/index.mdx", "reports/audits/session-library-approval.md", REPORT("TASK-1124")],
    SCHEMA_OK + ["Există minimum 36 de ședințe complete și validate.", "Ambele ritmuri săptămânale sunt acoperite."],
    volume="VOLUME-07", units=4)

# Volumes VIII–X.
late_volumes = {
    "12": ("VOLUME-08", ["Meciul ca mediu de învățare", "Observarea individuală și colectivă", "Evaluare fără reducerea la scor", "Feedbackul după meci", "Instrumente și rubrici de progres"], ["TASK-1124", "TASK-0204"]),
    "13": ("VOLUME-09", ["Parteneriatul cu părinții", "Regulamentul copiilor și al părinților", "Disciplină și proceduri echitabile", "Safeguarding și responsabilități", "Raportarea îngrijorărilor și incidentele", "Incluziune, demnitate și limite profesionale"], ["TASK-0104", "TASK-0109", "TASK-0780"]),
    "14": ("VOLUME-10", ["Folosirea manualului digital pe teren", "Diagrame și animații ca instrumente de predare", "Colectarea responsabilă a observațiilor", "Accesibilitate, offline și întreținere"], ["TASK-0408", "TASK-1024", "TASK-1124"]),
}
for phase, (volume, chapters, deps) in late_volumes.items():
    base = int(phase) * 100
    chapter_ids = []
    for i, title in enumerate(chapters, 1):
        tid = f"TASK-{base+i:04d}"
        chapter_ids.append(tid)
        add(tid, f"Capitol — {title}", f"PHASE-{phase}", deps,
            [f"content/volume-{int(phase)-4:02d}/chapter-{i:02d}.mdx", REPORT(tid)],
            CHAPTER_OK, volume=volume, units=5)
    audit = f"TASK-{base + len(chapters) + 1:04d}"
    repair = f"TASK-{base + len(chapters) + 2:04d}"
    add(audit, f"Audit independent {volume}", f"PHASE-{phase}", chapter_ids,
        [f"reports/audits/{volume.lower()}-audit.md", REPORT(audit)], SCHEMA_OK + ["Auditul acoperă toate porțile aplicabile."],
        volume=volume, units=3)
    add(repair, f"Reparare și aprobare {volume}", f"PHASE-{phase}", [audit],
        [f"reports/audits/{volume.lower()}-approval.md", REPORT(repair)], SCHEMA_OK + ["Defectele critice și mari sunt închise."],
        volume=volume, units=3)
    volume_last[phase] = repair

# Integration, builds and delivery.
final_tasks = [
    ("1501", "Integrarea celor zece volume și a navigației", [volume_last[p] for p in ["05","06","07","08","09","12","13","14"]] + ["TASK-1024","TASK-1124"], ["content/manual-manifest.json"], 5),
    ("1502", "Sincronizarea glosarului și terminologiei", ["TASK-1501"], ["data/glossary.json"], 3),
    ("1503", "Bibliografia verificabilă și exporturile de citare", ["TASK-1501","TASK-0110"], ["content/bibliography.mdx","dist/editable/bibliography.json"], 3),
    ("1504", "Indexul tematic și referințele încrucișate", ["TASK-1501","TASK-1502"], ["content/index.mdx"], 3),
    ("1505", "Audit editorial transversal și deduplicare", ["TASK-1502","TASK-1503","TASK-1504"], ["reports/audits/editorial-integration.md"], 4),
    ("1506", "Repararea auditului editorial transversal", ["TASK-1505"], ["reports/audits/editorial-integration-approval.md"], 3),
    ("1601", "Build web static complet", ["TASK-1506"], ["dist/web/index.html"], 5),
    ("1602", "Testarea offline, rutelor, linkurilor și activelor", ["TASK-1601"], ["reports/build/web-integrity.md"], 4),
    ("1603", "Audit browser desktop, mobil și accesibilitate", ["TASK-1602"], ["reports/build/browser-audit.md"], 4),
    ("1604", "Repararea și aprobarea buildului web", ["TASK-1603"], ["reports/build/web-approval.md"], 3),
    ("1701", "Generarea PDF complet", ["TASK-1604"], ["dist/pdf/manual-u11.pdf"], 5),
    ("1702", "Audit vizual PDF și paritate cu animațiile", ["TASK-1701"], ["reports/build/pdf-visual-audit.md"], 4),
    ("1703", "Repararea și aprobarea PDF-ului", ["TASK-1702"], ["reports/build/pdf-approval.md"], 3),
    ("1801", "Generarea resurselor editabile", ["TASK-1604","TASK-1703"], ["dist/editable/manifest.json"], 4),
    ("1802", "Licențe, atribuiri și inventar de active", ["TASK-1801","TASK-1503"], ["dist/LICENSES.md","dist/asset-inventory.json"], 3),
    ("1901", "Suită completă de teste din surse curate", ["TASK-1604","TASK-1703","TASK-1802"], ["reports/testing/full-suite.md"], 5),
    ("1902", "Audit de securitate, confidențialitate și date locale", ["TASK-1901"], ["reports/testing/security-privacy.md"], 3),
    ("1903", "Audit independent al pragurilor cantitative și calitative", ["TASK-1901"], ["reports/testing/deliverables-audit.md"], 4),
    ("1904", "Repararea regresiilor de release candidate", ["TASK-1902","TASK-1903"], ["reports/testing/release-candidate-approval.md"], 4),
    ("2001", "Audit final independent Gate 0–9", ["TASK-1904"], ["reports/final-audit/FINAL_AUDIT.md"], 5),
    ("2002", "Repararea constatărilor auditului final", ["TASK-2001"], ["reports/final-audit/REPAIR_RECORD.md"], 4),
    ("2003", "Verdictul final verificabil", ["TASK-2002"], ["reports/final-audit/FINAL_REPORT.md"], 4),
    ("2101", "Crearea arhivei de livrare și a hashurilor", ["TASK-2003"], ["dist/manual-u11-release.zip","dist/SHA256SUMS.txt"], 3),
    ("2102", "Dezarhivarea și retestarea în director curat", ["TASK-2101"], ["reports/final-audit/CLEAN-ROOM-TEST.md"], 4),
    ("2103", "Manifestul final de livrare", ["TASK-2102"], ["dist/RELEASE_MANIFEST.json"], 2),
]
for code, title, deps, outputs, units in final_tasks:
    tid = f"TASK-{code}"
    add(tid, title, f"PHASE-{code[:2]}", deps, outputs + [REPORT(tid)],
        SCHEMA_OK + ["Porțile de calitate aplicabile sunt documentate cu verdict.", "Orice defect critic sau mare blochează continuarea."],
        priority="CRITICAL" if code.startswith(("20","21")) else "HIGH", units=units)

# PHASE-22 — Gold Standard vertical slice: "Sprijinul și unghiul de pasă".
# Supersedes (does not replace/delete) the earlier, architecturally-misaligned
# TASK-0410-TASK-0418 chain (docs/gold-standard/GOLD_STANDARD_READINESS_AUDIT.md,
# DEC-0044) — that chain targets a standalone prototype page and depends on two
# never-built infrastructure tasks (TASK-0304 animation engine, TASK-0407
# Playwright harness). This chain instead reuses the already-FIELD_REVIEW_READY
# VOLUME-02 principles (spatiu-si-unghiuri, progresie-si-sprijin) as its concept/
# perception/decision foundation, and is the project's first real production of
# the exercise/session/assessment entity types (schemas existed, zero instances).
add("TASK-2201", "Gold Standard Readiness Audit — Sprijinul și unghiul de pasă", "PHASE-22", ["TASK-0810"],
    ["docs/gold-standard/GOLD_STANDARD_READINESS_AUDIT.md", REPORT("TASK-2201")],
    SCHEMA_OK + [
        "Matricea de pregătire acoperă toate dimensiunile cerute (dezvoltare, percepție, decizie, comunicare, principii de joc, metodologie, execuție tehnică, evaluare, arhitectură de exerciții/ședințe, semantică vizuală).",
        "Fiecare artefact prototip existent (lanțul TASK-0410-0418, fixture-urile din data/fixtures/) este clasificat explicit KEEP/KEEP_WITH_REPAIR/REBUILD/SUPERSEDE/REMOVE, nu presupus corect.",
        "Graful de taskuri creat este minim și derivat din audit, nu speculativ."
    ],
    volume="GOLD-STANDARD", units=2, status="DONE")
add("TASK-2202", "Cercetare execuție tehnică și harta propoziție-dovadă", "PHASE-22", ["TASK-2201"],
    ["research/dossiers/gold-standard-support-angle.md", "research/sources.json", "research/claims.json", REPORT("TASK-2202")],
    SCHEMA_OK + [
        "Fiecare sursă nouă e verificată extern (CrossRef/doi.org, cel puțin două rute de identitate pentru sursele fundamentale) înainte de a fi citată.",
        "Harta propoziție-dovadă acoperă execuția tehnică (orientare la recepție, prima atingere) — singurul gap RESEARCH_REQUIRED identificat de audit.",
        "Niciun unghi sau distanță exactă nu este prezentat ca regulă universală validată științific."
    ],
    volume="GOLD-STANDARD", units=3, status="READY")
add("TASK-2203", "Pachetul de concept Gold Standard (model de eroare/intervenție specific)", "PHASE-22", ["TASK-2202"],
    ["docs/gold-standard/CONCEPT_MODEL.md", REPORT("TASK-2203")],
    SCHEMA_OK + [
        "Reutilizează explicit principle-spatiu-si-unghiuri și principle-progresie-si-sprijin ca fundație, fără a le duplica sau contrazice.",
        "Taxonomia erorilor observabile separă explicit OBSERVAȚIA de CAUZELE POSIBILE.",
        "Modelul de intervenție nu inventează praguri de repetiție sau timp fără sursă."
    ],
    volume="GOLD-STANDARD", units=3, status="READY")
add("TASK-2204", "Sistemul de exerciții Gold Standard (prima producție reală)", "PHASE-22", ["TASK-2203"],
    ["data/exercises/", REPORT("TASK-2204")],
    SCHEMA_OK + [
        "Fiecare exercițiu validează contra schemas/exercise.schema.json.",
        "Numărul de exerciții e derivat din etapele de învățare necesare, nu dintr-o cotă istorică.",
        "Progresia 2v1->3v2->4v4 (dacă folosită) e justificată explicit pas cu pas (ce informație/decizie nouă apare), nu presupusă corectă."
    ],
    volume="GOLD-STANDARD", units=6, status="READY")
add("TASK-2205", "Sistemul de ședințe Gold Standard (prima producție reală)", "PHASE-22", ["TASK-2204"],
    ["data/sessions/", REPORT("TASK-2205")],
    SCHEMA_OK + [
        "Fiecare ședință validează contra schemas/session.schema.json.",
        "Fiecare activitate din ședință răspunde explicit la 'de ce e aici, acum'.",
        "Numărul de ședințe e justificat pedagogic, nu presupus (ex. '2 ședințe' din prototipul vechi)."
    ],
    volume="GOLD-STANDARD", units=4, status="READY")
add("TASK-2206", "Evaluare și transfer în meci Gold Standard (prima producție reală)", "PHASE-22", ["TASK-2205"],
    ["data/assessments/", REPORT("TASK-2206")],
    SCHEMA_OK + [
        "Fiecare instrument validează contra schemas/assessment.schema.json.",
        "Separă explicit succesul la sarcină de înțelegere/adaptabilitate și de transferul în meci.",
        "Nu folosește scoruri pseudo-precise (ex. '7.3/10')."
    ],
    volume="GOLD-STANDARD", units=3, status="READY")
add("TASK-2207", "Instrumente de teren și specificații vizuale tactice Gold Standard", "PHASE-22", ["TASK-2206"],
    ["docs/gold-standard/FIELD_TOOLS.md", "docs/gold-standard/TACTICAL_VISUAL_SPECS.md", REPORT("TASK-2207")],
    SCHEMA_OK + [
        "Fiecare instrument de teren trece testul de utilizabilitate (folosibil fără a citi un manual).",
        "Specificațiile vizuale nu implică un unghi/distanță exactă ca regulă validată fără etichetă explicită.",
        "Nu se ating fișierele de design freeze."
    ],
    volume="GOLD-STANDARD", units=3, status="READY")
add("TASK-2208", "Integrare web Gold Standard (Quick Mode + Deep Mode)", "PHASE-22", ["TASK-2207"],
    ["app/src/lib/content-bridge.ts", REPORT("TASK-2208")],
    SCHEMA_OK + [
        "Quick Mode și Deep Mode folosesc aceleași entități canonice, fără duplicare contradictorie.",
        "Toate relațiile (principiu-exercițiu, exercițiu-vizual, ședință-exercițiu) rezolvă la ID-uri reale.",
        "npm run build trece fără a modifica fișierele de design freeze."
    ],
    volume="GOLD-STANDARD", units=4, status="READY")
add("TASK-2209", "Audit independent Gold Standard", "PHASE-22", ["TASK-2208"],
    ["reports/audits/gold-standard-support-angle-audit.md", REPORT("TASK-2209")],
    SCHEMA_OK + [
        "Auditul e realizat separat de producție — nu combină verificarea cu munca de corectare.",
        "Un eșantion semnificativ de surse fundamentale e re-verificat extern independent.",
        "Verdictul este binar: PASS_FIELD_REVIEW_READY sau REPAIR_REQUIRED."
    ],
    volume="GOLD-STANDARD", units=3, status="READY")
add("TASK-2210", "Remediere Gold Standard (dacă REPAIR_REQUIRED)", "PHASE-22", ["TASK-2209"],
    ["reports/audits/gold-standard-support-angle-repair.md", REPORT("TASK-2210")],
    SCHEMA_OK + ["Toate constatările auditului sunt închise sau documentate explicit ca reziduale."],
    volume="GOLD-STANDARD", units=3, status="PENDING")
add("TASK-2211", "Pachetul de field review Gold Standard", "PHASE-22", ["TASK-2209"],
    ["docs/field-review/GOLD_STANDARD_SUPPORT_ANGLE_FIELD_REVIEW_PACKAGE.md", REPORT("TASK-2211")],
    SCHEMA_OK + [
        "Nu simulează rezultate de pilotare reală.",
        "Definește explicit ce NU se poate concluziona din pilot.",
        "Include matricea de decizie KEEP/MODIFY/REMOVE/RESEARCH_REQUIRED."
    ],
    volume="GOLD-STANDARD", units=2, status="READY")

# PHASE-23: pilotare reală de teren. Diferă fundamental de PHASE-22 — succesul nu se
# infera din validatoare/teste/build, ci exclusiv din date reale de teren, furnizate
# de utilizator. Runda 1 pregateste doar materialul de pilotare (fisa de teren,
# template de retur) si selecteaza felia minima (SES-0001: EX-0001-EX-0003) pentru a
# izola constatarile de utilizabilitate/pedagogice inainte de a expune intregul sistem
# (SES-0002: EX-0004/EX-0005). Task-urile de analiza/remediere ulterioare se creeaza
# doar din constatari reale, nu speculativ (nu exista inca in acest grafic).
add("TASK-2301", "Gold Standard Real Field Pilot — Runda 1 (pregătire)", "PHASE-23", ["TASK-2211"],
    ["docs/field-pilot/GOLD_STANDARD_SUPPORT_ANGLE_FIELD_SHEET_R1.md",
     "docs/field-pilot/PHASE23_FIELD_RETURN_TEMPLATE_R1.md", REPORT("TASK-2301")],
    SCHEMA_OK + [
        "Nu conține niciun rezultat de pilotare fabricat sau simulat.",
        "Selectează felia minimă coerentă pentru Runda 1, cu justificare explicită.",
        "Fișa de teren e utilizabilă în timp real de un antrenor care încă antrenează.",
        "Template-ul de retur conține exact informația necesară analizei, nimic inventat."
    ],
    volume="GOLD-STANDARD-PILOT", units=3, status="READY")

# PHASE-24: audit de paritate implementare produs. Constatare centrala: continutul
# canonic (25 capitole, 25 principii, sistemul Gold Standard complet) exista si e
# corect, dar navigarea primara a site-ului (antet, homepage, "Incepe aici") nu ducea
# la niciunul dintre ele -- ruta exclusiv catre 3 fixture-uri de dezvoltare. TASK-2401
# a remediat gap-ul critic la nivelul datelor (getPrimaryNavigation(), consumata direct
# de AppHeader.astro din git HEAD fara filtrare) si a adaugat un index real de
# principii + cross-linkuri intre volume. A descoperit si o divergenta majora
# HEAD-vs-working-tree pentru fisierele design-freeze (redesign vizual in lucru,
# niciodata comis), documentata dar nerezolvata autonom -- necesita decizie explicita
# a utilizatorului. TASK-2402 (audit independent) verifica separat, fara nicio
# implicare in remediere.
add("TASK-2401", "Audit de paritate implementare produs — canonic vs. web real", "PHASE-24", ["TASK-2301"],
    ["reports/audits/PRODUCT_IMPLEMENTATION_PARITY_AUDIT.md", REPORT("TASK-2401")],
    SCHEMA_OK + [
        "Inventarul canonic e construit inaintea inspectiei rutelor web, nu invers.",
        "Fiecare gap critic/major identificat are o clasificare de tip si severitate.",
        "Remedierea nu incalca design freeze-ul — nicio modificare CSS/structurala/vizuala.",
        "Navigarea globala duce la continut real de productie, nu la fixture-uri de dezvoltare."
    ],
    volume="PRODUCT-PARITY", units=5, status="DONE")
add("TASK-2402", "Audit independent de paritate implementare produs", "PHASE-24", ["TASK-2401"],
    ["reports/audits/product-implementation-parity-reaudit.md", REPORT("TASK-2402")],
    SCHEMA_OK + [
        "Auditul e realizat separat de remediere — nu combina verificarea cu munca de corectare.",
        "Reconstruieste inventarul independent, nu doar verifica taskurile marcate DONE.",
        "Verdictul este binar: PASS_PRODUCT_PARITY_V1 sau REPAIR_REQUIRED."
    ],
    volume="PRODUCT-PARITY", units=4, status="READY")
# TASK-2402 a dat REPAIR_REQUIRED: un singur defect blocant, precis delimitat de
# auditor -- HomepageHero.astro linia 16, href catre ruta fixture stricata in loc de
# /gold-standard/rapid, contrazicand afirmatia de reparare "functionala" din raportul
# TASK-2401/DEC-0048. Remediere mecanica de o linie, aplicata exact cum a specificat
# auditorul -- verificata prin build propriu si grep pe HTML-ul generat, nu doar prin
# citire de cod.
add("TASK-2403", "Remediere: CTA hero homepage către ruta fixture", "PHASE-24", ["TASK-2402"],
    [REPORT("TASK-2403")],
    SCHEMA_OK + ["Toate constatările auditului TASK-2402 sunt închise sau documentate explicit ca reziduale."],
    volume="PRODUCT-PARITY", units=1, status="PENDING")

# PHASE-25: recovery and final product-acceptance gate after the product
# hardening commits that followed b109920.
add("TASK-2501", "Field-pilot product hardening — recuperare, validare si acceptanta finala", "PHASE-25", ["TASK-2403"],
    ["plans/TASK-2501-field-pilot-product-hardening.md",
     "reports/audits/PHASE25_FIELD_PILOT_PRODUCT_ACCEPTANCE.md", REPORT("TASK-2501")],
    SCHEMA_OK + [
        "Produsul curent este reproductibil integral din git HEAD.",
        "ASM-0001, indexul de volume si vizualurile EX-0001—EX-0003 sunt randate si accesibile.",
        "Navigarea publica nu expune /design-system si continutul vizibil nu contine tokenuri de autor sau jargon intern brut.",
        "Auditul final este browser-first, dupa ultima remediere, la 1440, 1280, 768 si 390 px.",
        "Verdictul final este binar: PASS_FIELD_PILOT_PRODUCT_ACCEPTANCE sau REPAIR_REQUIRED."
    ],
    volume="FIELD-PILOT-PRODUCT", units=6, status="IN_PROGRESS",
    validations=["python scripts/validate_content.py --strict", "python scripts/validate_project.py",
                 "python scripts/generate_task_registry.py --check", "python -m unittest discover -s tests -p \"test_*.py\"",
                 "npm.cmd run check", "npm.cmd run build"])

add("TASK-2601", "Vercel Preview staging — deploy si acceptanta live", "PHASE-26", ["TASK-2501"],
    ["plans/TASK-2601-vercel-staging.md", "reports/deployments/TASK-2601-vercel-staging.md", REPORT("TASK-2601")],
    SCHEMA_OK + [
        "Deploy-ul este Preview, fara domeniu custom, analytics sau functionalitati comerciale.",
        "Deploymentul corespunde unui commit identificat si este reproductibil din Git.",
        "Rutele, activele si viewporturile 1440/1280/768/390 sunt verificate pe URL-ul Vercel live.",
        "Nu sunt publicate secrete, date despre copii sau rezultate de pilot fabricate."
    ],
    volume="VERCEL-STAGING", units=4, status="DONE",
    validations=["python scripts/validate_content.py --strict", "python scripts/validate_project.py",
                 "python scripts/generate_task_registry.py --check", "python -m unittest discover -s tests -p \"test_*.py\"",
                 "npm.cmd run check", "npm.cmd run build"])


add("TASK-2701", "Premium Product Master Audit - experienta, continut si arhitectura comerciala", "PHASE-27", ["TASK-2601"],
    ["plans/TASK-2701-premium-product-master-audit.md", "reports/audits/MANUALFC_PREMIUM_PRODUCT_MASTER_AUDIT.md", REPORT("TASK-2701")],
    SCHEMA_OK + [
        "Auditul este browser-first pe produsul live la 1440/1280/768/390 si acopera intregul inventar public.",
        "Benchmarkul extern foloseste surse actuale si separa faptele verificate de ipoteze si idei de produs.",
        "Raportul include matrice page-by-page, scoring, template-uri V2, wireframe-uri, monetizare, top 20, top 5 si backlog prioritizat.",
        "Nu implementeaza redesignul, functionalitati comerciale sau continut factual neverificat."
    ],
    volume="PREMIUM-PRODUCT-AUDIT", units=12, status="DONE",
    validations=["python scripts/validate_content.py --strict", "python scripts/validate_project.py",
                 "python scripts/generate_task_registry.py --check"])

add("TASK-2702", "Wave-1 production hygiene - separarea suprafetelor interne", "PHASE-27", ["TASK-2701"],
    ["plans/TASK-2702-production-hygiene.md", "docs/architecture/PRODUCTION_ROUTE_CLASSIFICATION.md", REPORT("TASK-2702")],
    SCHEMA_OK + [
        "Rutele interne si fixture nu sunt generate in buildul public, dar activele lor de QA raman pastrate.",
        "Suprafetele publice si 404 nu pierd continut canonic sau navigare functionala.",
        "Buildul si browserul confirma absenta rutelor interne din produsul public."
    ], volume="PREMIUM-WAVE-1", units=3, status="DONE",
    validations=["python scripts/validate_content.py --strict", "python scripts/validate_project.py",
                 "python scripts/generate_task_registry.py --check", "python -m unittest discover -s tests -p \"test_*.py\"",
                 "npm.cmd run check", "npm.cmd run build"])
add("TASK-2703", "Wave-1 IA V2 si terminologie orientata spre sarcina", "PHASE-27", ["TASK-2702"],
    ["plans/TASK-2703-ia-v2-terminology.md", "docs/architecture/INFORMATION_ARCHITECTURE_V2.md", REPORT("TASK-2703")],
    SCHEMA_OK + [
        "Navigarea primara foloseste intentii clare ale antrenorului si pastreaza toate destinatiile reale.",
        "Termenii interni raman secundari, iar etichetele publice sunt inteligibile fara documentatie tehnica.",
        "Headerul, footerul si paginile-index sunt coerente la desktop si mobil."
    ], volume="PREMIUM-WAVE-1", units=3, status="DONE",
    validations=["python scripts/validate_content.py --strict", "python scripts/validate_project.py",
                 "python scripts/generate_task_registry.py --check", "python -m unittest discover -s tests -p \"test_*.py\"",
                 "npm.cmd run check", "npm.cmd run build"])
add("TASK-2704", "Wave-1 Presentation Layer V2 pentru principii si exercitii", "PHASE-27", ["TASK-2703"],
    ["plans/TASK-2704-presentation-layer-v2.md", "docs/architecture/PRESENTATION_LAYER_V2.md", REPORT("TASK-2704")],
    SCHEMA_OK + [
        "Principiile si exercitiile au un rezumat actionabil deasupra pliului, derivat exclusiv din date canonice.",
        "Stratul progresiv pastreaza fundamentarea completa, limitele, dovezile si transferul in joc.",
        "Template-urile sunt responsive, accesibile, imprimabile si pregatite structural pentru un viitor Field Mode fara a-l simula."
    ], volume="PREMIUM-WAVE-1", units=5, status="DONE",
    validations=["python scripts/validate_content.py --strict", "python scripts/validate_project.py",
                 "python scripts/generate_task_registry.py --check", "python -m unittest discover -s tests -p \"test_*.py\"",
                 "npm.cmd run check", "npm.cmd run build"])
add("TASK-2705", "Wave-2 Group Configurator - logistica de teren determinista 8-18 copii", "PHASE-27", ["TASK-2717"],
    ["plans/TASK-2705-group-configurator.md", "docs/architecture/GROUP_CONFIGURATOR.md",
     "app/src/lib/group-configurator.ts", "app/src/pages/gold-standard/configurator.astro",
     "schemas/exercise.schema.json", REPORT("TASK-2705")],
    SCHEMA_OK + [
        "Configuratiile pentru 8/10/12/14/16/18 copii, la 1 si 2 antrenori, sunt derivate determinist din datele canonice ale exercitiilor, nu inventate.",
        "Marimea grupului ramane egala cu players.total al exercitiului; relatia numerica nu este alterata pentru a se potrivi unui efectiv.",
        "Orice regula fara fundamentare de cercetare (rotatie, aranjament spatial, pozitionarea antrenorului) este etichetata explicit PRACTICE_HEURISTIC.",
        "Pagina este verificata browser-first la 1440/768/390 fara erori de consola si fara overflow orizontal al paginii."
    ], volume="PREMIUM-WAVE-2", units=4, status="DONE",
    validations=["python scripts/validate_content.py --strict", "python scripts/validate_project.py",
                 "python scripts/generate_task_registry.py --check", "python -m unittest discover -s tests -p \"test_*.py\"",
                 "npm.cmd run check", "npm.cmd run build"])
add("TASK-2706", "Wave-2 contingente operationale SES-0001/SES-0002 + Wave-2.1 harta terenului si variante de 60 min", "PHASE-27", ["TASK-2705"],
    ["plans/TASK-2706-session-contingencies.md", "app/src/pages/gold-standard/sedinte/[id].astro",
     "app/src/pages/gold-standard/sedinte/[id]/mod-teren.astro",
     "app/src/lib/surface-map.ts", "app/src/components/SurfaceMap.astro",
     "schemas/session.schema.json", REPORT("TASK-2706")],
    SCHEMA_OK + [
        "players_range al ambelor sedinte acopera 8-18 copii.",
        "Fiecare sedinta are minimum 5 scenarii operationale reale (intarziati, spatiu redus, material insuficient, exercitiu esuat, tranzitie lunga), fiecare cu ghidare etichetata explicit PRACTICE_HEURISTIC.",
        "Ghidarea reutilizeaza campuri canonice deja existente (too_small_signs, transition_logistics, regression) in loc sa dubleze continut.",
        "Pagina de sedinta este verificata browser-first fara erori de consola si fara overflow orizontal.",
        "Harta terenului (Wave-2.1) este derivata determinist din Group Configurator pentru orice efectiv 8-18 si 1/2 antrenori, fara model de logistica paralel.",
        "Fiecare sedinta are o varianta de 60 minute cu motiv explicit per segment (ce se reduce, de ce, ce se pastreaza), pastrand neschimbata varianta canonica de 75 minute.",
        "Totalurile variantei de 60 minute insumeaza exact 60, fara goluri sau suprapuneri intre segmente."
    ], volume="PREMIUM-WAVE-2", units=3, status="DONE",
    validations=["python scripts/validate_content.py --strict", "python scripts/validate_project.py",
                 "python scripts/generate_task_registry.py --check", "python -m unittest discover -s tests -p \"test_*.py\"",
                 "npm.cmd run check", "npm.cmd run build"])
add("TASK-2707", "Wave-2 vizuale EX-0004/EX-0005 si Fise de teren", "PHASE-27", ["TASK-2706"],
    ["plans/TASK-2707-visuals-field-cards.md", "app/src/components/TacticalDiagram.astro",
     "app/src/components/FieldCard.astro", "app/src/pages/gold-standard/fise-de-teren.astro",
     REPORT("TASK-2707")],
    SCHEMA_OK + [
        "EX-0004 si EX-0005 au diagrame tactice reale, nu declaratii de lipsa.",
        "Diagrama EX-0005 este etichetata explicit ca moment reprezentativ posibil, nu forma obligatorie, consecvent cu jocul liber fara constrangeri artificiale.",
        "Fisele de teren acopera toate cele 5 exercitii cu campurile minime cerute, fara raționale sau surse.",
        "Paginile sunt verificate browser-first fara erori de consola si fara overflow orizontal."
    ], volume="PREMIUM-WAVE-2", units=4, status="DONE",
    validations=["python scripts/validate_content.py --strict", "python scripts/validate_project.py",
                 "python scripts/generate_task_registry.py --check", "python -m unittest discover -s tests -p \"test_*.py\"",
                 "npm.cmd run check", "npm.cmd run build"])
add("TASK-2711", "Wave-2 fundatie multimedia - standard pe niveluri si prototip buclă tactică", "PHASE-27", ["TASK-2707"],
    ["plans/TASK-2711-multimedia-foundation.md", "docs/architecture/MULTIMEDIA_FOUNDATION.md",
     "app/src/components/TacticalLoop.astro", REPORT("TASK-2711")],
    SCHEMA_OK + [
        "Standardul pe 5 niveluri este documentat, cu starea reala a fiecarui nivel, nu simulata.",
        "Prototipul Nivelul 1 este o animatie CSS/SVG functionala, verificata prin interactiune reala (pauza/reda) si prin page.emulateMedia pentru prefers-reduced-motion, nu doar vizual.",
        "Nu se fabrica niciun fisier video sau filmare reala.",
        "Diagrama statica existenta ramane referinta principala, neatinsa."
    ], volume="PREMIUM-WAVE-2", units=3, status="DONE",
    validations=["python scripts/validate_content.py --strict", "python scripts/validate_project.py",
                 "python scripts/generate_task_registry.py --check", "python -m unittest discover -s tests -p \"test_*.py\"",
                 "npm.cmd run check", "npm.cmd run build"])
add("TASK-2710", "Wave-2 Field Mode - navigare de sedinta pe teren, un segment o data", "PHASE-27", ["TASK-2711"],
    ["plans/TASK-2710-field-mode.md", "app/src/pages/gold-standard/sedinte/[id]/mod-teren.astro",
     REPORT("TASK-2710")],
    SCHEMA_OK + [
        "Modul teren este activat explicit dintr-un CTA vizibil, nu auto-detectat.",
        "Un singur segment este vizibil o data, cu bara fixa Inapoi/Cronometru/Urmatorul, toate controalele minim 48px.",
        "Toate datele provin din aceeasi sursa canonica (getGoldStandardSession/getGoldStandardExercise) ca paginile normale, fara continut paralel.",
        "Testat prin interactiune reala in browser (click, scroll, JS evaluate), nu doar vizual; defectele gasite sunt reparate si documentate."
    ], volume="PREMIUM-WAVE-2", units=5, status="DONE",
    validations=["python scripts/validate_content.py --strict", "python scripts/validate_project.py",
                 "python scripts/generate_task_registry.py --check", "python -m unittest discover -s tests -p \"test_*.py\"",
                 "npm.cmd run check", "npm.cmd run build"])
add("TASK-2708", "Wave-3 taxonomie, cercetare si biblioteca canonica de probleme observabile", "PHASE-27", ["TASK-2710"],
    ["plans/TASK-2708-problem-taxonomy.md", "schemas/problem.schema.json", "data/problems/problem-library.json",
     "docs/architecture/PROBLEM_TAXONOMY.md", "docs/architecture/PROBLEM_KNOWLEDGE_GRAPH.md",
     "docs/architecture/PROBLEM_EVIDENCE_MAPPING.md", "docs/architecture/PROBLEM_MULTIMEDIA_MAPPING.md", REPORT("TASK-2708")],
    SCHEMA_OK + [
        "Biblioteca contine minimum 8 probleme observabile, exact 3 flagship si separa explicit observatia de ipoteza.",
        "Fiecare problema are test cu o singura variabila, mesaj pentru copil, limita de interpretare si verificare de transfer.",
        "Graful nu are referinte rupte catre principii, exercitii, sedinte, evaluari sau dovezi.",
        "Limbajul comportamental nu medicalizeaza si nu transforma corelatia in diagnostic."
    ], volume="PREMIUM-WAVE-3", units=5, status="DONE",
    validations=["python scripts/validate_content.py --strict", "python -m unittest tests.test_task2708_problem_graph -v",
                 "python scripts/generate_task_registry.py --check", "npm.cmd run check", "npm.cmd run build"])
add("TASK-2709", "Wave-3 Decision / Problem Engine MVP", "PHASE-27", ["TASK-2708"],
    ["plans/TASK-2709-decision-engine.md", "app/src/lib/problem-library.ts", "app/src/pages/rezolva-pe-teren/index.astro",
     "app/src/pages/rezolva-pe-teren/[slug].astro", REPORT("TASK-2709")],
    SCHEMA_OK + [
        "Antrenorul ajunge de la observatie la un test si un mesaj actionabil in maximum 30 de secunde.",
        "Fluxurile flagship leaga configuratorul, sedinta, Field Mode, evaluarea si verificarea transferului fara continut duplicat.",
        "Interfata mobil-first comunica explicit incertitudinea si nu diagnosticheaza copilul."
    ], volume="PREMIUM-WAVE-3", units=6, status="DONE",
    validations=["python scripts/validate_content.py --strict", "python -m unittest discover -s tests -p \"test_*.py\"",
                 "npm.cmd run check", "npm.cmd run build"])
add("TASK-2712", "Wave-3 cautare lexicala, filtre deterministe si discovery", "PHASE-27", ["TASK-2709"],
    ["plans/TASK-2712-discovery.md", "docs/architecture/SEARCH_DISCOVERY.md", "app/src/lib/discovery-index.ts",
     "app/src/pages/cauta.astro", REPORT("TASK-2712")],
    SCHEMA_OK + [
        "Cautarea statica acopera probleme, principii, exercitii, sedinte si evaluari si explica potrivirea.",
        "Filtrele expuse au diferentiere reala, stare fara rezultate si reset accesibil.",
        "Scenariul 12 jucatori / 20 minute conduce determinist la o actiune compatibila cu configuratorul."
    ], volume="PREMIUM-WAVE-3", units=5, status="DONE",
    validations=["python scripts/validate_content.py --strict", "python -m unittest discover -s tests -p \"test_*.py\"",
                 "npm.cmd run check", "npm.cmd run build"])
add("TASK-2801", "Wave-4 release Wave-3, final product ledger si arhitectura", "PHASE-28", ["TASK-2712"],
    ["plans/PHASE-28-wave4-coach-operating-system.md", "docs/product/FINAL_PRODUCT_FEATURE_LEDGER.md",
     "docs/architecture/COACH_OPERATING_SYSTEM.md", REPORT("TASK-2801")],
    SCHEMA_OK + ["Deploymentul Wave-3 acceptat este promovat fara rebuild si trece smoke Production.",
                 "Ledgerul final pastreaza toate capabilitatile si o stare explicita.",
                 "Arhitectura exclude PII despre copii si separa domeniul de adapterul de persistenta."],
    volume="PREMIUM-WAVE-4", units=4, status="DONE")
add("TASK-2802", "Wave-4 Session Workspace si workflow local persistent", "PHASE-28", ["TASK-2801"],
    ["app/src/lib/coach-state.ts", "app/src/components/CoachActions.astro", "app/src/pages/spatiul-meu/index.astro",
     "app/src/pages/spatiul-meu/sedinta.astro", "docs/architecture/SESSION_WORKSPACE.md",
     "tests/test_task2802_workspace.py", REPORT("TASK-2802")],
    SCHEMA_OK + ["Workspace stocheaza referinte si configurare, nu copie de continut canonic.",
                 "Salvate, favorite, recente si continua supravietuiesc unui reload.",
                 "Builderul respinge referinte rupte si totaluri inconsistente.",
                 "Starea corupta din localStorage revine fail-closed la adapter, fara stare fabricata.",
                 "Controalele generate dinamic respecta tinta de atins de minimum 44px la 390px."],
    volume="PREMIUM-WAVE-4", units=8, status="DONE")
add("TASK-2803", "Wave-4 reflectie post-sedinta si transfer loop", "PHASE-28", ["TASK-2802"],
    ["app/src/pages/spatiul-meu/reflectie.astro", "app/src/lib/coach-state.ts", "app/src/pages/gold-standard/sedinte/[id]/mod-teren.astro",
     "app/src/pages/spatiul-meu/index.astro", "docs/architecture/ASSESSMENT_REFLECTION_LOOP.md",
     "tests/test_task2803_reflection.py", REPORT("TASK-2803")],
    SCHEMA_OK + ["Field Mode are finalizare clara catre reflectie.", "Starea calitativa nu pretinde precizie inexistenta.",
                 "Urmatoarea vizita poate continua decizia din referinte canonice stabile.",
                 "Performanta in sarcina si transferul in joc sunt distinctii separate, niciodata confundate.",
                 "Recomandarea urmatorului pas este determinista, nu text liber generat.",
                 "Extensia de stare v1 pastreaza integral datele TASK-2802 existente."],
    volume="PREMIUM-WAVE-4", units=5, status="DONE")
add("TASK-2804", "Wave-4 multimedia extins si coach explainer pipeline", "PHASE-28", ["TASK-2803"],
    ["app/src/components/ConceptLoop.astro", "app/src/components/ExerciseSequenceAnimation.astro",
     "app/src/components/CoachExplainerScript.astro", "app/src/lib/media-registry.ts",
     "data/media/media-registry.json", "schemas/media-registry.schema.json",
     "docs/architecture/MULTIMEDIA_PRODUCTION_PIPELINE.md", "tests/test_task2804_media.py", REPORT("TASK-2804")],
    SCHEMA_OK + ["Cele 3 probleme flagship si EX-0001-EX-0005 au media semantic justificata.",
                 "Miscarea pastreaza specificatia canonica si are reduced-motion/static fallback.",
                 "Nu este fabricata filmare reala.",
                 "Registrul media este fail-closed: referinte canonice rupte opresc buildul.",
                 "EX-0004/EX-0005 raman fara animatie noua, cu motiv documentat explicit."],
    volume="PREMIUM-WAVE-4", units=5, status="DONE")
add("TASK-2805", "Wave-4 PWA, offline field pack si platform boundaries", "PHASE-28", ["TASK-2804"],
    ["public/manifest.webmanifest", "public/sw.js", "app/src/lib/offline-pack.ts",
     "docs/architecture/OFFLINE_ACCOUNT_ENTITLEMENT.md", "tests/test_task2805_offline.py", REPORT("TASK-2805")],
    SCHEMA_OK + ["O sedinta pregatita ramane utilizabila in Field Mode offline.",
                 "Reflectia offline nu este suprascrisa silentios.", "Entitlementul se rezolva central si nu ascunde safety."],
    volume="PREMIUM-WAVE-4", units=6, status="DONE")
add("TASK-2806", "Wave-4 Preview, audit live si baseline", "PHASE-28", ["TASK-2805"],
    ["reports/audits/MANUALFC_WAVE4_BROWSER_ACCEPTANCE.md", REPORT("TASK-2806")],
    SCHEMA_OK + ["Candidatul curat trece auditul live la 1440/1280/768/390.",
                 "Fluxul de 5 minute, revenirea si offline Field Mode trec in browser.",
                 "Baseline-ul este inghetat numai cu 0 Critical si 0 Major."],
    volume="PREMIUM-WAVE-4", units=4, status="DONE")
add("TASK-2901", "Knowledge Architecture master", "PHASE-29", ["TASK-2806"],
    ["docs/knowledge/MANUALFC_KNOWLEDGE_ARCHITECTURE.md"],
    SCHEMA_OK + ["Cei trei piloni si bucla canonica de invatare sunt definiti.",
                 "Documentul citeaza explicit precedentul canonic existent, nu duplica concepte."],
    volume="KNOWLEDGE-FOUNDATION", units=3, status="DONE")
add("TASK-2902", "Pedagog Domain Map", "PHASE-29", ["TASK-2901"],
    ["docs/knowledge/PEDAGOG_DOMAIN_MAP.md"],
    SCHEMA_OK + ["Cele 12 domenii au subdomenii, prioritati si legaturi de competenta.",
                 "Fiecare domeniu leaga explicit spre Antrenorul si spre practica existenta."],
    volume="KNOWLEDGE-FOUNDATION", units=4, status="DONE")
add("TASK-2903", "Coach Domain Map", "PHASE-29", ["TASK-2901"],
    ["docs/knowledge/COACH_DOMAIN_MAP.md"],
    SCHEMA_OK + ["Cele 34 de domenii au comportamente observabile si anti-tipare.",
                 "Fiecare domeniu leaga explicit spre Pedagogul si spre practica existenta."],
    volume="KNOWLEDGE-FOUNDATION", units=4, status="DONE")
add("TASK-2904", "Cadrele de competenta Pedagog si Antrenor", "PHASE-29", ["TASK-2902", "TASK-2903"],
    ["docs/knowledge/PEDAGOG_COMPETENCY_FRAMEWORK.md", "docs/knowledge/COACH_COMPETENCY_FRAMEWORK.md"],
    SCHEMA_OK + ["Fiecare competenta are indicatori comportamentali, anti-tipare si baza de dovada.",
                 "Fara scor numeric, fara niveluri de rang.",
                 "ID-urile sunt stabile si independente de UI."],
    volume="KNOWLEDGE-FOUNDATION", units=5, status="DONE")
add("TASK-2905", "Theory-to-Practice Contract", "PHASE-29", ["TASK-2904"],
    ["docs/knowledge/THEORY_TO_PRACTICE_CONTRACT.md"],
    SCHEMA_OK + ["Lantul cercetare-comportament-practica-reflectie este complet.",
                 "Cele 4 teste de calitate (orice subiect, teorie-teren x3, teren-teorie, fara silozuri) trec.",
                 "Contractul de 18 intrebari existent este reconciliat explicit, nu inlocuit."],
    volume="KNOWLEDGE-FOUNDATION", units=5, status="DONE")
add("TASK-2906", "Knowledge Graph Specification", "PHASE-29", ["TASK-2905"],
    ["docs/knowledge/KNOWLEDGE_GRAPH_SPECIFICATION.md"],
    SCHEMA_OK + ["Extinde graful Wave-3 existent, nu creeaza un graf paralel.",
                 "Fiecare relatie are scop semantic explicit (intelegere/descoperire/practica/validare)."],
    volume="KNOWLEDGE-FOUNDATION", units=3, status="DONE")
add("TASK-2907", "Evidence Classification System si Research Production Pipeline", "PHASE-29", ["TASK-2901"],
    ["docs/knowledge/EVIDENCE_CLASSIFICATION_SYSTEM.md", "docs/knowledge/RESEARCH_PRODUCTION_PIPELINE.md"],
    SCHEMA_OK + ["Vocabularul de dovezi reutilizeaza claim-registry.schema.json existent, nu creeaza unul concurent.",
                 "Pipeline-ul de cercetare formalizeaza research/dossiers/ existent."],
    volume="KNOWLEDGE-FOUNDATION", units=4, status="DONE")
add("TASK-2908", "Content Depth Standard, Existing Product Mapping, Schema Impact Analysis", "PHASE-29", ["TASK-2905"],
    ["docs/knowledge/CONTENT_DEPTH_STANDARD.md", "docs/knowledge/EXISTING_PRODUCT_KNOWLEDGE_MAPPING.md", "docs/knowledge/KNOWLEDGE_SCHEMA_IMPACT_ANALYSIS.md"],
    SCHEMA_OK + ["Cele 4 straturi de profunzime raman un singur obiect canonic, nu patru articole.",
                 "Fiecare schimbare de schema propusa este aditiva si optionala.",
                 "Niciun exercitiu/sesiune/problema existenta nu devine invalida."],
    volume="KNOWLEDGE-FOUNDATION", units=5, status="DONE")
add("TASK-2909", "KPI Model si Research Roadmap", "PHASE-29", ["TASK-2908"],
    ["docs/knowledge/KNOWLEDGE_AND_COMPETENCY_KPI_MODEL.md", "docs/knowledge/PHASE30_RESEARCH_ROADMAP.md"],
    SCHEMA_OK + ["K1-K4 raman dimensiuni separate, fara procent global.",
                 "Roadmap-ul prioritizeaza pe dependenta, nu alfabetic."],
    volume="KNOWLEDGE-FOUNDATION", units=3, status="DONE")
add("TASK-2910", "PHASE-29 acceptance si Knowledge Foundation baseline", "PHASE-29", ["TASK-2906", "TASK-2907", "TASK-2909"],
    ["reports/audits/MANUALFC_PHASE29_KNOWLEDGE_FOUNDATION_ACCEPTANCE.md", "docs/product/FINAL_PRODUCT_FEATURE_LEDGER.md"],
    SCHEMA_OK + ["Auditul de compatibilitate cu produsul final nu gaseste niciun blocaj nou.",
                 "Runtime-ul Wave-4 acceptat ramane neschimbat.",
                 "Baseline-ul de arhitectura este inghetat separat de baseline-ul Wave-4."],
    volume="KNOWLEDGE-FOUNDATION", units=3, status="DONE")
add("TASK-3001", "Dosar de cercetare: dezvoltarea copilului 10-11 ani", "PHASE-30", ["TASK-2910"],
    ["research/dossiers/CHILD_DEVELOPMENT_10_11_R1.md"],
    SCHEMA_OK + ["Sursele sunt verificate real prin cautare externa, nu inventate.",
                 "Fiecare claim marcheaza populatia si contextul sportiv aplicabil."],
    volume="RESEARCH-FOUNDATION", units=4, status="DONE")
add("TASK-3002", "Dosar de cercetare: motivatie si autonomie", "PHASE-30", ["TASK-2910"],
    ["research/dossiers/MOTIVATION_AUTONOMY_R1.md"],
    SCHEMA_OK + ["Susinerea autonomiei nu este redusa la 'pune mereu intrebari'.",
                 "Fiecare claim marcheaza populatia si contextul sportiv aplicabil."],
    volume="RESEARCH-FOUNDATION", units=4, status="DONE")
add("TASK-3003", "Dosar de cercetare: atentie si incarcatura cognitiva", "PHASE-30", ["TASK-2910"],
    ["research/dossiers/ATTENTION_COGNITIVE_LOAD_R1.md"],
    SCHEMA_OK + ["Nicio regula fixa de tip 'X secunde' nu este introdusa fara sursa.",
                 "Fiecare claim marcheaza populatia si contextul sportiv aplicabil."],
    volume="RESEARCH-FOUNDATION", units=4, status="DONE")
add("TASK-3004", "Dosar de cercetare: feedback", "PHASE-30", ["TASK-2910"],
    ["research/dossiers/FEEDBACK_R1.md"],
    SCHEMA_OK + ["Literatura de motor learning este separata explicit de cea pedagogica.",
                 "Fiecare claim marcheaza populatia si contextul sportiv aplicabil."],
    volume="RESEARCH-FOUNDATION", units=4, status="DONE")
add("TASK-3005", "Dosar de cercetare: chestionare si descoperire ghidata", "PHASE-30", ["TASK-2910"],
    ["research/dossiers/QUESTIONING_GUIDED_DISCOVERY_R1.md"],
    SCHEMA_OK + ["Chestionarea este tratata ca instrument situational, nu superioritate morala.",
                 "Fiecare claim marcheaza populatia si contextul sportiv aplicabil."],
    volume="RESEARCH-FOUNDATION", units=4, status="DONE")
add("TASK-3006", "Dosar de cercetare: interventia antrenorului (cand NU intervine)", "PHASE-30", ["TASK-2910"],
    ["research/dossiers/COACH_INTERVENTION_R1.md"],
    SCHEMA_OK + ["Sloganul 'antrenorii buni nu vorbesc' este respins explicit de dovezi.",
                 "Fiecare claim marcheaza populatia si contextul sportiv aplicabil."],
    volume="RESEARCH-FOUNDATION", units=4, status="DONE")
add("TASK-3007", "Dosar de cercetare: cadre de achizitie a deprinderii", "PHASE-30", ["TASK-2910"],
    ["research/dossiers/SKILL_ACQUISITION_FRAMEWORKS_R1.md"],
    SCHEMA_OK + ["Nu se adopta o singura tabara teoretica in mod doctrinar.",
                 "Fiecare claim marcheaza populatia si contextul sportiv aplicabil."],
    volume="RESEARCH-FOUNDATION", units=4, status="DONE")
add("TASK-3008", "Dosar de cercetare: perceptie-decizie-actiune", "PHASE-30", ["TASK-2910"],
    ["research/dossiers/PERCEPTION_DECISION_ACTION_R1.md"],
    SCHEMA_OK + ["Falsa dihotomie tehnica-izolata vs. joc-integral este evitata explicit.",
                 "Fiecare claim marcheaza populatia si contextul sportiv aplicabil."],
    volume="RESEARCH-FOUNDATION", units=4, status="DONE")
add("TASK-3009", "Dosar de cercetare: transfer si retinere", "PHASE-30", ["TASK-2910"],
    ["research/dossiers/TRANSFER_RETENTION_R1.md"],
    SCHEMA_OK + ["Distinctia performanta-vs-invatare este centrala si explicita.",
                 "FIELD_INPUT_REQUIRED la nivel de produs (PHASE-23) ramane neschimbat."],
    volume="RESEARCH-FOUNDATION", units=4, status="DONE")
add("TASK-3010", "Matrice de acoperire, matricea de competente, glosar, registru de mituri", "PHASE-30",
    ["TASK-3001", "TASK-3002", "TASK-3003", "TASK-3004", "TASK-3005", "TASK-3006", "TASK-3007", "TASK-3008", "TASK-3009"],
    ["docs/knowledge/research/COMPETENCY_EVIDENCE_MATRIX_R1.md",
     "docs/knowledge/research/PEDAGOG_RESEARCH_COVERAGE_MATRIX_R1.md",
     "docs/knowledge/research/COACH_RESEARCH_COVERAGE_MATRIX_R1.md",
     "docs/knowledge/research/RESEARCH_TERMINOLOGY_GLOSSARY.md",
     "docs/knowledge/research/MANUALFC_RESEARCH_OVERCLAIM_WATCHLIST.md",
     "research/sources.json", "research/claims.json", "research/citations.json"],
    SCHEMA_OK + ["Registrele de cercetare extinse raman valide fata de schemele existente.",
                 "Domeniile ne-cercetate sunt marcate explicit NOT_RESEARCHED, nu ascunse."],
    volume="RESEARCH-FOUNDATION", units=6, status="DONE")
add("TASK-3011", "Sinteze cross-cluster si audit de aliniere a continutului curent", "PHASE-30", ["TASK-3010"],
    ["docs/knowledge/research/LEARNING_AND_COACHING_SYNTHESIS_R1.md",
     "docs/knowledge/research/GOOD_COACH_BEHAVIOUR_SYNTHESIS_R1.md"],
    SCHEMA_OK + ["Auditul de aliniere nu modifica niciun fisier de continut runtime.",
                 "Sinteza de competente nu inventeaza legaturi acolo unde nu exista dovada."],
    volume="RESEARCH-FOUNDATION", units=5, status="DONE")
add("TASK-3012", "PHASE-30 acceptance si Research Foundation baseline", "PHASE-30", ["TASK-3011"],
    ["reports/audits/MANUALFC_PHASE30_RESEARCH_FOUNDATION_ACCEPTANCE.md", "docs/product/FINAL_PRODUCT_FEATURE_LEDGER.md"],
    SCHEMA_OK + ["Auditul independent prin esantion de claim-uri nu gaseste nicio nepotrivire.",
                 "Runtime-ul ramane neschimbat, confirmat explicit."],
    volume="RESEARCH-FOUNDATION", units=3, status="DONE")
add("TASK-3013", "Dosar de cercetare: relatia pedagogica", "PHASE-30", ["TASK-3012"],
    ["research/dossiers/PEDAGOGICAL_RELATIONSHIP_R1.md"],
    SCHEMA_OK + ["Framing-ul relatie != prietenie este sustinut de dovezi reale.",
                 "Fiecare claim marcheaza populatia si contextul sportiv aplicabil."],
    volume="RESEARCH-FOUNDATION-W2", units=4, status="DONE")
add("TASK-3014", "Dosar de cercetare: dinamica de grup", "PHASE-30", ["TASK-3012"],
    ["research/dossiers/GROUP_DYNAMICS_YOUTH_SPORT_R1.md"],
    SCHEMA_OK + ["Nici 'competitia strica dezvoltarea' nici 'competitia construieste caracterul' nu sunt acceptate necondiionat.",
                 "Fiecare claim marcheaza populatia si contextul sportiv aplicabil."],
    volume="RESEARCH-FOUNDATION-W2", units=4, status="DONE")
add("TASK-3015", "Dosar de cercetare: parintii", "PHASE-30", ["TASK-3012"],
    ["research/dossiers/PARENTS_YOUTH_SPORT_R1.md"],
    SCHEMA_OK + ["Primul dosar ManualFC pe acest subiect; nicio implicare parentala nu este etichetata daunatoare fara dovada.",
                 "Fiecare claim marcheaza populatia si contextul sportiv aplicabil."],
    volume="RESEARCH-FOUNDATION-W2", units=4, status="DONE")
add("TASK-3016", "Dosar de cercetare: dezvoltarea emotionala si reglarea", "PHASE-30", ["TASK-3012"],
    ["research/dossiers/EMOTIONAL_DEVELOPMENT_AND_REGULATION_R1.md"],
    SCHEMA_OK + ["Raspunsurile emotionale normale ale copilului nu sunt medicalizate.",
                 "Fiecare claim marcheaza populatia si contextul sportiv aplicabil."],
    volume="RESEARCH-FOUNDATION-W2", units=4, status="DONE")
add("TASK-3017", "Dosar de cercetare: reflectia antrenorului", "PHASE-30", ["TASK-3012"],
    ["research/dossiers/COACH_REFLECTIVE_PRACTICE_R1.md"],
    SCHEMA_OK + ["Reflectia nu este presupusa a imbunatati automat practica.",
                 "Fiecare claim marcheaza populatia si contextul sportiv aplicabil."],
    volume="RESEARCH-FOUNDATION-W2", units=4, status="DONE")
add("TASK-3018", "Dosar de cercetare: auto-evaluarea antrenorului", "PHASE-30", ["TASK-3012"],
    ["research/dossiers/COACH_SELF_EVALUATION_R1.md"],
    SCHEMA_OK + ["Efectul Dunning-Kruger este verificat activ, nu presupus aplicabil la coaching.",
                 "Fiecare claim marcheaza populatia si contextul sportiv aplicabil."],
    volume="RESEARCH-FOUNDATION-W2", units=4, status="DONE")
add("TASK-3019", "Dosar de cercetare: dezvoltarea profesionala a antrenorului", "PHASE-30", ["TASK-3012"],
    ["research/dossiers/COACH_PROFESSIONAL_DEVELOPMENT_R1.md"],
    SCHEMA_OK + ["Ierarhia place-a-invatat-comportament-beneficiu este aplicata consecvent.",
                 "Niciun Coach Score sau clasament nu este propus."],
    volume="RESEARCH-FOUNDATION-W2", units=4, status="DONE")
add("TASK-3020", "Matrice R2, registru de mituri extins, integrare registru real", "PHASE-30",
    ["TASK-3013", "TASK-3014", "TASK-3015", "TASK-3016", "TASK-3017", "TASK-3018", "TASK-3019"],
    ["docs/knowledge/research/PEDAGOG_RESEARCH_COVERAGE_MATRIX_R2.md",
     "docs/knowledge/research/COACH_RESEARCH_COVERAGE_MATRIX_R2.md",
     "docs/knowledge/research/COMPETENCY_EVIDENCE_MATRIX_R2.md",
     "docs/knowledge/research/MANUALFC_RESEARCH_OVERCLAIM_WATCHLIST.md",
     "research/sources.json", "research/claims.json", "research/citations.json"],
    SCHEMA_OK + ["Matricele R1 raman ca istoric, nu sunt sterse.",
                 "Registrele extinse raman valide fata de schemele existente dupa deduplicare."],
    volume="RESEARCH-FOUNDATION-W2", units=6, status="DONE")
add("TASK-3021", "Sinteze cross-cluster si porti de disponibilitate V2", "PHASE-30", ["TASK-3020"],
    ["docs/knowledge/research/PEDAGOGICAL_ENVIRONMENT_SYNTHESIS_R1.md",
     "docs/knowledge/research/COACH_LEARNING_AND_DEVELOPMENT_SYNTHESIS_R1.md"],
    SCHEMA_OK + ["Portile Reflection/Field Mode/Session/Gold Standard V2 sunt evaluate explicit.",
                 "Niciun runtime nu este atins de evaluarile de disponibilitate."],
    volume="RESEARCH-FOUNDATION-W2", units=5, status="DONE")
add("TASK-3022", "PHASE-30 Wave-2 acceptance si baseline", "PHASE-30", ["TASK-3021"],
    ["reports/audits/MANUALFC_PHASE30_WAVE2_RESEARCH_FOUNDATION_ACCEPTANCE.md", "docs/product/FINAL_PRODUCT_FEATURE_LEDGER.md"],
    SCHEMA_OK + ["Auditul independent prin esantion de claim-uri nu gaseste nicio nepotrivire.",
                 "Portile Pedagogul V1/Antrenorul V1 primesc verdict onest, nu inflat."],
    volume="RESEARCH-FOUNDATION-W2", units=3, status="DONE")
add("TASK-3023", "Dosar de cercetare: comunicare pedagogica generala", "PHASE-30", ["TASK-3022"],
    ["research/dossiers/GENERAL_PEDAGOGICAL_COMMUNICATION_R1.md"],
    SCHEMA_OK + ["Comunicarea nu e redusa la un slogan universal de tip 'vorbeste mai putin'.",
                 "Raportul 5:1 lauda-critica respins ca folclor necitat."],
    volume="RESEARCH-FOUNDATION-W3", units=4, status="DONE")
add("TASK-3024", "Dosare de cercetare: diferente individuale si diferentiere", "PHASE-30", ["TASK-3022"],
    ["research/dossiers/INDIVIDUAL_DIFFERENCES_IN_YOUTH_COACHING_R1.md",
     "research/dossiers/DIFFERENTIATION_AND_CHALLENGE_R1.md"],
    SCHEMA_OK + ["Nicio eticheta diagnostica sau de abilitate fixa nu este introdusa.",
                 "Regula '85%' respinsa explicit ca netransferabila din alt domeniu."],
    volume="RESEARCH-FOUNDATION-W3", units=5, status="DONE")
add("TASK-3025", "Dosar de cercetare: metacognitia copilului", "PHASE-30", ["TASK-3022"],
    ["research/dossiers/CHILD_METACOGNITION_AND_REFLECTION_R1.md"],
    SCHEMA_OK + ["Auto-raportul copilului nu este tratat ca dovada obiectiva de invatare.",
                 "Doua surse directe U11-fotbal identificate si verificate."],
    volume="RESEARCH-FOUNDATION-W3", units=4, status="DONE")
add("TASK-3026", "Dosar de cercetare: identitatea si rolul antrenorului", "PHASE-30", ["TASK-3022"],
    ["research/dossiers/COACH_IDENTITY_AND_ROLE_R1.md"],
    SCHEMA_OK + ["Filosofia declarata nu este presupusa a schimba automat comportamentul.",
                 "Granitele de rol (nu terapeut, nu substitut de parinte) sunt explicite."],
    volume="RESEARCH-FOUNDATION-W3", units=4, status="DONE")
add("TASK-3027", "Dosare de cercetare: design de sedinta si planificare pe termen mediu", "PHASE-30", ["TASK-3022"],
    ["research/dossiers/YOUTH_SESSION_DESIGN_R1.md",
     "research/dossiers/YOUTH_MEDIUM_TERM_PLANNING_R1.md"],
    SCHEMA_OK + ["Nicio formula numerica universala nu este inventata.",
                 "LTAD reconfirmat fara statut de standard de aur validat."],
    volume="RESEARCH-FOUNDATION-W3", units=5, status="DONE")
add("TASK-3028", "Dosar de cercetare: organizare si timp activ", "PHASE-30", ["TASK-3022"],
    ["research/dossiers/COACHING_ORGANIZATION_AND_ACTIVE_TIME_R1.md"],
    SCHEMA_OK + ["Pozitionarea antrenorului formalizata onest ca PRACTICE_HEURISTIC, nu stiinta manufacturata.",
                 "Timp activ mai mult nu este presupus automat egal cu invatare mai buna."],
    volume="RESEARCH-FOUNDATION-W3", units=4, status="DONE")
add("TASK-3029", "Matrice R3 finale si integrare registru", "PHASE-30",
    ["TASK-3023", "TASK-3024", "TASK-3025", "TASK-3026", "TASK-3027", "TASK-3028"],
    ["docs/knowledge/research/PEDAGOG_RESEARCH_COVERAGE_MATRIX_R3.md",
     "docs/knowledge/research/COACH_RESEARCH_COVERAGE_MATRIX_R3.md",
     "docs/knowledge/research/COMPETENCY_EVIDENCE_MATRIX_R3.md",
     "research/sources.json", "research/claims.json", "research/citations.json"],
    SCHEMA_OK + ["Toate cele 12 domenii Pedagogul au acoperire de fundatie.",
                 "Toate cele 34 domenii Antrenorul au stare explicita, niciunul NOT_RESEARCHED."],
    volume="RESEARCH-FOUNDATION-W3", units=6, status="DONE")
add("TASK-3030", "Sinteze finale si definitii Pedagogul/Antrenorul", "PHASE-30", ["TASK-3029"],
    ["docs/knowledge/research/PEDAGOGUL_RESEARCH_SYNTHESIS_V1.md",
     "docs/knowledge/research/ANTRENORUL_RESEARCH_SYNTHESIS_V1.md"],
    SCHEMA_OK + ["Definitiile Pedagog/Antrenor sunt comportamentale, nu marketing.",
                 "Modelul de suprapunere/granita este explicit."],
    volume="RESEARCH-FOUNDATION-W3", units=4, status="DONE")
add("TASK-3031", "Blueprint-uri de autorizare PHASE-31/32", "PHASE-30", ["TASK-3030"],
    ["docs/knowledge/PHASE31_PEDAGOGUL_AUTHORING_BLUEPRINT.md",
     "docs/knowledge/PHASE32_ANTRENORUL_AUTHORING_BLUEPRINT.md"],
    SCHEMA_OK + ["Niciun blueprint nu contine proza finala de lectie.",
                 "Harta de legaturi incrucisate Pedagog-Antrenor este completa."],
    volume="RESEARCH-FOUNDATION-W3", units=5, status="DONE")
add("TASK-3032", "Audit de granita a dovezilor si K1-K3", "PHASE-30", ["TASK-3031"],
    ["reports/audits/MANUALFC_PHASE30_WAVE3_RESEARCH_FOUNDATION_ACCEPTANCE.md"],
    SCHEMA_OK + ["Toate cele 6 lanturi teorie-practica trasate raman complete.",
                 "Golurile de context romanesc si de antrenor comunitar sunt semnalate explicit."],
    volume="RESEARCH-FOUNDATION-W3", units=4, status="DONE")
add("TASK-3033", "Acceptanta finala PHASE-30 si baseline", "PHASE-30", ["TASK-3032"],
    ["reports/audits/MANUALFC_PHASE30_WAVE3_RESEARCH_FOUNDATION_ACCEPTANCE.md", "docs/product/FINAL_PRODUCT_FEATURE_LEDGER.md"],
    SCHEMA_OK + ["Portile Pedagogul V1/Antrenorul V1 primesc verdict onest READY_WITH_LIMITATIONS.",
                 "PHASE-31/32 raman explicit neautorizate."],
    volume="RESEARCH-FOUNDATION-W3", units=3, status="DONE")
add("TASK-3101", "PHASE-31 preflight si inspectia arhitecturii de continut", "PHASE-31", ["TASK-3033"],
    ["reports/audits/MANUALFC_PHASE31_PEDAGOGUL_V1_ACCEPTANCE.md"],
    SCHEMA_OK + ["Integritatea registrelor de cercetare verificata inainte de redactare.",
                 "5 din 12 capitole planificate gasite deja existente, evitand duplicarea."],
    volume="PEDAGOGUL-V1", units=3, status="DONE")
add("TASK-3102", "Redactarea celor 5 capitole noi Pedagogul (CH-0106-CH-0110)", "PHASE-31", ["TASK-3101"],
    ["content/volume-01/chapter-06.mdx", "content/volume-01/chapter-07.mdx",
     "content/volume-01/chapter-08.mdx", "content/volume-01/chapter-09.mdx",
     "content/volume-01/chapter-10.mdx"],
    SCHEMA_OK + ["Toate cele 13 familii de competente Pedagogul au acum capitol-casa.",
                 "Fiecare capitol leaga explicit la dosarul de cercetare PHASE-30 sursa."],
    volume="PEDAGOGUL-V1", units=8, status="DONE")
add("TASK-3103", "Expunerea in produs a celor 5 capitole noi", "PHASE-31", ["TASK-3102"],
    ["app/src/pages/volum/01/[chapter].astro", "app/src/pages/volum/01/index.astro",
     "content/volume-01/manifest.json", "data/content/volumes/volume-01.json"],
    SCHEMA_OK + ["npm run check si npm run build trec curat.",
                 "Toate cele 10 rute raspund 200, un singur main per document."],
    volume="PEDAGOGUL-V1", units=5, status="DONE")
add("TASK-3104", "Actualizarea testelor existente si cele trei audituri de continut", "PHASE-31", ["TASK-3103"],
    ["tests/test_volume_01.py", "tests/test_task0507_volume01_approval.py"],
    SCHEMA_OK + ["Auditul factual pe esantion nu gaseste nicio discrepanta.",
                 "Toate cele patru teste de calitate (prea subtire/prea academic/doar teorie/practica fara motiv) trec."],
    volume="PEDAGOGUL-V1", units=5, status="DONE")
add("TASK-3105", "Acceptanta PHASE-31 Pedagogul V1 si baseline", "PHASE-31", ["TASK-3104"],
    ["reports/audits/MANUALFC_PHASE31_PEDAGOGUL_V1_ACCEPTANCE.md", "docs/product/FINAL_PRODUCT_FEATURE_LEDGER.md"],
    SCHEMA_OK + ["Scopul a fost adaptat onest fata de blueprint, documentat explicit.",
                 "RUNTIME_CHANGED: YES, verificat prin build real, nu presupus."],
    volume="PEDAGOGUL-V1", units=3, status="DONE")
add("TASK-3301", "Cercetare Gate 1: cognitive load, progressive disclosure, retrieval practice, accesibilitate, case-based learning, benchmarking", "EDU-PAGE-SYSTEM-V1", ["TASK-3105"],
    ["docs/ux/MANUALFC_EDUCATIONAL_PAGE_RESEARCH.md", "docs/ux/LEARNING_UX_EVIDENCE_MATRIX.md"],
    SCHEMA_OK + ["6 clustere de cercetare independente, fiecare cu surse verificate real.",
                 "Watchlist explicit al principiilor NESusținute de dovezi (acordeon, F-pattern, andragogie)."],
    volume="EDU-PAGE-SYSTEM-V1", units=8, status="DONE")
add("TASK-3302", "Gate 2: principii de design trasabile la dovezi", "EDU-PAGE-SYSTEM-V1", ["TASK-3301"],
    ["docs/ux/MANUALFC_EDUCATIONAL_DESIGN_PRINCIPLES.md"],
    SCHEMA_OK + ["17 principii, fiecare cu evidenta/mecanism/implicatie/aplicatie/limita.",
                 "Sectiune explicita de principii respinse."],
    volume="EDU-PAGE-SYSTEM-V1", units=3, status="DONE")
add("TASK-3303", "Gate 3-4: arhitecturi concurente, decizie, standard canonic, contract de componente", "EDU-PAGE-SYSTEM-V1", ["TASK-3302"],
    ["docs/ux/MANUALFC_EDUCATIONAL_PAGE_STANDARD_V1.md", "docs/ux/EDUCATIONAL_COMPONENT_CONTRACT.md",
     "docs/ux/MANUALFC_EDUCATIONAL_PAGE_USER_TEST_PROTOCOL.md"],
    SCHEMA_OK + ["3 arhitecturi comparate onest, un castigator declarat explicit (Model C Hybrid).",
                 "Inventarul celor 23 de componente existente auditat inainte de a construi altele noi."],
    volume="EDU-PAGE-SYSTEM-V1", units=6, status="DONE")
add("TASK-3304", "Implementarea componentelor educationale (6 noi/extinse) si repararea defectului de hoisting MDX", "EDU-PAGE-SYSTEM-V1", ["TASK-3303"],
    ["app/src/components/ChapterOrganizer.astro", "app/src/components/ExplanationToggle.astro",
     "app/src/components/ElaborationBlock.astro", "app/src/components/RevealPrompt.astro",
     "app/src/components/QuickRecall.astro", "app/src/components/PredictPrompt.astro",
     "app/src/components/SectionNavigator.astro", "app/src/lib/educational-page.ts",
     "app/src/styles/educational-page.css", "app/src/layouts/BaseLayout.astro"],
    SCHEMA_OK + ["Defect real descoperit si documentat: componentele Astro folosite din MDX in content/ (in afara srcDir) nu beneficiaza de script/style hoisting.",
                 "Reparat prin centralizare in BaseLayout.astro, nu prin ocolire silentioasa."],
    volume="EDU-PAGE-SYSTEM-V1", units=6, status="DONE")
add("TASK-3305", "Pilot pe 3 capitole reprezentative (CH-0101, CH-0103, CH-0106) si reparare defect de fidelitate", "EDU-PAGE-SYSTEM-V1", ["TASK-3304"],
    ["content/volume-01/chapter-01.mdx", "content/volume-01/chapter-03.mdx", "content/volume-01/chapter-06.mdx"],
    SCHEMA_OK + ["Defect real gasit si reparat: primul paragraf de scenariu din CH-0103 fusese pierdut la prima editare -- verificat linie cu linie contra HEAD, reparat, reverificat.",
                 "0 linii originale lipsa dupa reparare, confirmat programatic pe toate cele 3 capitole pilot."],
    volume="EDU-PAGE-SYSTEM-V1", units=5, status="DONE")
add("TASK-3306", "Rollout complet la celelalte 7 capitole (CH-0102,0104,0105,0107,0108,0109,0110)", "EDU-PAGE-SYSTEM-V1", ["TASK-3305"],
    ["content/volume-01/chapter-02.mdx", "content/volume-01/chapter-04.mdx", "content/volume-01/chapter-05.mdx",
     "content/volume-01/chapter-07.mdx", "content/volume-01/chapter-08.mdx", "content/volume-01/chapter-09.mdx",
     "content/volume-01/chapter-10.mdx"],
    SCHEMA_OK + ["ExplanationToggle aplicat doar unde exista o sectiune reala de elaborare (Justificarea completa) -- CH-0101/0102/0105 nu au, corect omis, nu fortat.",
                 "0 linii originale lipsa dupa aplicare, confirmat programatic pe toate cele 10 capitole."],
    volume="EDU-PAGE-SYSTEM-V1", units=7, status="DONE")
add("TASK-3307", "QA finala: validatori, teste, build, verificare structurala HTTP pe toate cele 10 capitole plus regresie", "EDU-PAGE-SYSTEM-V1", ["TASK-3306"],
    ["reports/audits/MANUALFC_EDUCATIONAL_PAGE_PILOT_ACCEPTANCE.md"],
    SCHEMA_OK + ["npm run check 0 erori, npm run build 92 pagini, pytest 505/505, validate_project.py 0 erori.",
                 "AXE = NOT_RUN raportat onest -- Playwright MCP indisponibil, verificare doar structurala HTTP."],
    volume="EDU-PAGE-SYSTEM-V1", units=4, status="DONE")
add("TASK-3308", "Candidat curat, incercare de deployment Preview, acceptanta finala si baseline", "EDU-PAGE-SYSTEM-V1", ["TASK-3307"],
    ["reports/audits/MANUALFC_EDUCATIONAL_PAGE_SYSTEM_FINAL_ACCEPTANCE.md", "docs/product/FINAL_PRODUCT_FEATURE_LEDGER.md"],
    SCHEMA_OK + ["PREVIEW_LIVE_ACCEPTANCE_BLOCKED raportat onest -- Vercel CLI neinstalat, fara VERCEL_TOKEN, sesiune non-interactiva.",
                 "PHASE-32 ramane explicit neautorizat."],
    volume="EDU-PAGE-SYSTEM-V1", units=3, status="DONE")
add("TASK-3309", "Acceptanta finala LIVE_BROWSER: audit real cu Playwright/Chromium pe Preview, reparare defect H1, reparare corupere working-tree preexistenta", "EDU-PAGE-SYSTEM-V1", ["TASK-3308"],
    ["reports/audits/MANUALFC_EDUCATIONAL_PAGE_SYSTEM_FINAL_ACCEPTANCE.md", "app/src/pages/volum/01/[chapter].astro"],
    SCHEMA_OK + ["Browser real (Chrome, conectat prin CDP la o sesiune autentificata de utilizator) folosit, nu doar vercel curl.",
                 "Defect MAJOR real gasit (H1 taiat la 390px pe CH-0106) si reparat, redeploy, reaudit -- CRITICAL=0, MAJOR=0.",
                 "Corupere reala preexistenta a 4 fisiere din working tree (0 bytes) gasita si reparata din HEAD, neascunsa.",
                 "Axe real rulat (nu NOT_RUN): 0 violari pe 5 pagini reprezentative."],
    volume="EDU-PAGE-SYSTEM-V1", units=6, status="DONE")
add("TASK-3310", "Hygiene patch: reparare overflow orizontal 100vw pe principii/[slug].astro", "PRE-PHASE-32-HYGIENE", ["TASK-3309"],
    ["app/src/pages/principii/[slug].astro", "reports/audits/MANUALFC_PRE_PHASE32_PRINCIPLE_OVERFLOW_REPAIR.md"],
    SCHEMA_OK + ["Defect reprodus intai (nu presupus din raportul anterior), root cause confirmat empiric (bara de scroll, discrepanta constanta 15px).",
                 "Doua incercari de reparare esuate documentate onest (overflow:clip nu functioneaza; --scrollbar-w calc(100vw - 100%) se re-rezolva gresit in var()).",
                 "Fix functional (masurare JS + proprietate CSS in pixeli ficsi), 0 overflow pe 5 rute x 4 viewport-uri, 0 regresie pe Educational Page System V1 (ramane inghetat la aff2017).",
                 "Commit izolat, doar fisierul reparat -- fara amestec de documentatie in commit-ul de runtime."],
    volume="PRE-PHASE-32-HYGIENE", units=3, status="DONE")
add("TASK-3401", "Reconciliere continut existent si corectare referinte stale in COACH_COMPETENCY_FRAMEWORK.md / COACH_DOMAIN_MAP.md", "PHASE-32", ["TASK-3310"],
    ["docs/knowledge/COACH_COMPETENCY_FRAMEWORK.md", "docs/knowledge/COACH_DOMAIN_MAP.md"],
    SCHEMA_OK + ["Verificare directa a continutului real din volume-03/volume-04 inainte de a autoriza autorat nou.",
                 "Referinte stale (ch-0801/0802/0805) corectate la fisierele reale (chapter-01/02/05.mdx, CH-0401/0402/0405)."],
    volume="PHASE-32", units=2, status="DONE")
add("TASK-3402", "Gold Standard V2 mapping pentru EX-0001-0005/SES-0001-0002, fara migrare de schema", "PHASE-32", ["TASK-3401"],
    ["docs/knowledge/GOLD_STANDARD_V2_MAPPING.md"],
    SCHEMA_OK + ["Mapare per exercitiu/sedinta derivata din campurile JSON reale, nu inventata.",
                 "Nicio migrare de schema runtime -- doar documentatie de mapare."],
    volume="PHASE-32", units=3, status="DONE")
add("TASK-3403", "Redactarea celor 9 capitole noi Antrenorul (CH-0307/0308/0309/0310, CH-0407/0408/0409/0410/0411)", "PHASE-32", ["TASK-3401"],
    ["content/volume-03/chapter-07.mdx", "content/volume-03/chapter-08.mdx", "content/volume-03/chapter-09.mdx",
     "content/volume-03/chapter-10.mdx", "content/volume-04/chapter-07.mdx", "content/volume-04/chapter-08.mdx",
     "content/volume-04/chapter-09.mdx", "content/volume-04/chapter-10.mdx", "content/volume-04/chapter-11.mdx"],
    SCHEMA_OK + ["Fiecare capitol scris dintr-un dosar de cercetare real, cu contractul de 19 intrebari Antrenorul respectat.",
                 "Fara Coach Score/ranking; sectiuni noi (Legatura cu pedagogia, Competentele de coaching, Reflectia antrenorului) prezente in toate."],
    volume="PHASE-32", units=9, status="DONE")
add("TASK-3404", "Integrarea in produs: manifeste, rute, index-uri de volum si componente Educational Page System V1", "PHASE-32", ["TASK-3403"],
    ["content/volume-03/manifest.json", "content/volume-04/manifest.json",
     "app/src/pages/volum/03/[chapter].astro", "app/src/pages/volum/04/[chapter].astro",
     "app/src/pages/volum/03/index.astro", "app/src/pages/volum/04/index.astro"],
    SCHEMA_OK + ["ChapterOrganizer, SectionNavigator si QuickRecall aplicate pe toate cele 9 capitole noi.",
                 "npm run build genereaza toate cele 19 rute de capitol (10 volume-03 + 11 volume-04) fara eroare."],
    volume="PHASE-32", units=4, status="DONE")
add("TASK-3405", "Audit de acoperire a competentelor (18 COACH-C, legatura Pedagog-Antrenor) si 6 lanturi teorie-practica", "PHASE-32", ["TASK-3404"],
    ["reports/audits/MANUALFC_PHASE32_ANTRENORUL_V1_ACCEPTANCE.md"],
    SCHEMA_OK + ["Toate cele 18 COACH-C insotite de status de dovada, legatura Pedagog si legatura de practica.",
                 "Cel putin 6 lanturi teorie-practica testate si documentate."],
    volume="PHASE-32", units=4, status="DONE")
add("TASK-3406", "QA completa: validatori, build, teste, audit de continut pe esantion si QA real in browser", "PHASE-32", ["TASK-3404"],
    ["reports/audits/MANUALFC_PHASE32_ANTRENORUL_V1_ACCEPTANCE.md"],
    SCHEMA_OK + ["npm run check/build, pytest, validate_project.py toate 0 erori.",
                 "QA real in browser (Playwright/CDP) pe rutele Antrenorul noi, cu regresie zero pe Pedagogul/Principii/EX-0001.",
                 "Defect real (H1 overflow, propagat la volume-02/03/04) gasit si reparat, nu ascuns; fals pozitiv de cache investigat si infirmat."],
    volume="PHASE-32", units=5, status="DONE")
add("TASK-3407", "Deployment Preview, acceptanta finala PHASE-32 si baseline ANTRENORUL_V1", "PHASE-32", ["TASK-3405", "TASK-3406"],
    ["reports/audits/MANUALFC_PHASE32_ANTRENORUL_V1_ACCEPTANCE.md", "docs/product/FINAL_PRODUCT_FEATURE_LEDGER.md"],
    SCHEMA_OK + ["Commit exact redeployat ca Vercel Preview si reverificat live.",
                 "Baseline MANUALFC_ANTRENORUL_V1_BASELINE inghetat fara a suprascrie baseline-urile anterioare."],
    volume="PHASE-32", units=3, status="DONE")
add("TASK-3501", "Guvernanta preflight, integritate cercetare, inspectie as-built Gold Standard", "PHASE-33", ["TASK-3407"],
    ["reports/audits/MANUALFC_PHASE33_GOLD_STANDARD_V2_ACCEPTANCE.md"],
    SCHEMA_OK + ["Baseline ANTRENORUL_V1 verificat direct (git cat-file, merge-base), nu presupus din prompt.",
                 "BYTE_INTEGRITY/JSON_PARSE/SCHEMA = PASS pe research/sources.json, claims.json, citations.json."],
    volume="PHASE-33", units=2, status="DONE")
add("TASK-3502", "Migrare aditiva de schema Gold Standard V2 (exercise/session) si validator dedicat", "PHASE-33", ["TASK-3501"],
    ["schemas/exercise.schema.json", "schemas/session.schema.json", "scripts/validate_gold_standard_v2.py"],
    SCHEMA_OK + ["Zero campuri noi in required -- continutul V1 existent ramane valid neschimbat.",
                 "Validatorul V2 verifica atat prezenta campurilor cat si existenta reala a fiecarui ID referentiat (PED-C/COACH-C/CH-xxxx/principle.*/ASM-xxxx)."],
    volume="PHASE-33", units=3, status="DONE")
add("TASK-3503", "Migrare EX-0001 (implementare de referinta) si gate-uri V2 complete", "PHASE-33", ["TASK-3502"],
    ["data/exercises/exercise-recunoasterea-umbrei-defensive.json", "app/src/pages/gold-standard/exercitii/[id].astro"],
    SCHEMA_OK + ["Schema + validator V2 + npm run check/build + pytest + audit real de browser (8 combinatii) toate PASS inainte de a migra EX-0002."],
    volume="PHASE-33", units=3, status="DONE")
add("TASK-3504", "Migrare EX-0002-EX-0005 (Gold Standard V2 complet pe cele 5 exercitii)", "PHASE-33", ["TASK-3503"],
    ["data/exercises/exercise-creeaza-optiunea-sub-presiune.json", "data/exercises/exercise-primeste-gata-sa-continui.json",
     "data/exercises/exercise-sprijin-cu-doi-coechipieri.json", "data/exercises/exercise-transferul-in-joc-mic.json"],
    SCHEMA_OK + ["Toate cele 5 exercitii V2 valideaza; un defect real (fraza «45 de grade» repetata in afara phrases_to_avoid) gasit de un test existent si reparat.",
                 "Audit real de browser: 24/24 combinatii (5 exercitii + ASM-0001 x 4 viewport-uri) PASS."],
    volume="PHASE-33", units=5, status="DONE")
add("TASK-3505", "Migrare SES-0001/0002 (obiective duale, Reflection V2), Field Mode V2, reparatii de legatura", "PHASE-33", ["TASK-3504"],
    ["data/sessions/session-introducere.json", "data/sessions/session-coordonare-si-transfer.json",
     "app/src/pages/gold-standard/sedinte/[id].astro", "app/src/pages/gold-standard/sedinte/[id]/mod-teren.astro"],
    SCHEMA_OK + ["Obiective duale copil/antrenor si reflection_v2 implementate in date SI in pagina, nu doar documentate.",
                 "Defect real preexistent de contrast de culoare (axe, 2.62 vs 4.5:1) gasit pe SES-0001/0002 si reparat, pentru ca bloca un gate propriu declarat al acestei faze.",
                 "Doua referinte plain-text (PRB-0003/EX-0003 in CH-0408, SES-0001/0002 in CH-0409) transformate in link-uri reale, inchizand un gol in traseul learning-first."],
    volume="PHASE-33", units=4, status="DONE")
add("TASK-3506", "QA completa PHASE-33: validatori, teste, build, audit real de browser pe matricea ceruta", "PHASE-33", ["TASK-3505"],
    ["reports/audits/MANUALFC_PHASE33_GOLD_STANDARD_V2_ACCEPTANCE.md"],
    SCHEMA_OK + ["11 rute x 4 viewport-uri = 44 combinatii PASS (0 overflow, 0 axe, 0 erori consola).",
                 "npm run check/build, pytest 505/505, validate_content.py, validate_gold_standard_v2.py toate 0 erori."],
    volume="PHASE-33", units=4, status="DONE")
add("TASK-3507", "Deployment Preview, acceptanta finala PHASE-33 si baseline GOLD_STANDARD_V2", "PHASE-33", ["TASK-3506"],
    ["reports/audits/MANUALFC_PHASE33_GOLD_STANDARD_V2_ACCEPTANCE.md"],
    SCHEMA_OK + ["Commit exact redeployat ca Vercel Preview si reverificat structural prin vercel curl (STRUCTURAL_PASS, browser local fara sesiune SSO -- declarat onest).",
                 "Baseline MANUALFC_GOLD_STANDARD_V2_BASELINE inghetat fara a suprascrie baseline-urile anterioare."],
    volume="PHASE-33", units=3, status="DONE")
add("TASK-3508", "Master Final-Product Gap Audit V2: as-built completion, multimedia gap, capacitate produs, scara de continut si pregatire comerciala", "CONTROL-PLANE", ["TASK-3507"],
    ["reports/audits/MANUALFC_MASTER_FINAL_PRODUCT_GAP_AUDIT_V2.md", "docs/product/MANUALFC_FINAL_PRODUCT_FEATURE_LEDGER_V2.md"],
    SCHEMA_OK + ["Audit strict read-only -- runtime, schema, continut si date neschimbate; verificat prin git status/diff inainte si dupa.",
                 "7 agenti de cercetare read-only dispatch-ati in paralel pentru dovezi; toata sinteza/scorarea facuta direct de asistent, nu delegata.",
                 "Confirma explicit ca 'Planificat: 60 exercitii, 36 sedinte...' e un target de task-batch-uri PENDING, nu progres real (5/60, 2/36).",
                 "USER_CONCERN_VIDEO_GAP = CONFIRMED, cu dovezi exhaustive (cautare repo-wide de fisiere video = 0 rezultate)."],
    volume="CONTROL-PLANE", units=3, status="DONE")
add("TASK-3601", "Master Integrity & Adversarial Product Audit: forensics, semantic integrity, repairs and final acceptance", "CONTROL-PLANE", ["TASK-3508"],
    ["plans/TASK-3601-master-integrity-audit.md",
     "reports/audits/MANUALFC_STAGE1_FORENSIC_AUDIT.md",
     "reports/audits/MANUALFC_STAGE2_ADVERSARIAL_USER_JOURNEY_AND_CHAOS_AUDIT.md",
     "reports/audits/MANUALFC_STAGE3_SEMANTIC_CONTENT_EVIDENCE_INTEGRITY_AUDIT.md",
     "reports/audits/MANUALFC_STAGE4_REPAIR_PROGRAM.md",
     "reports/audits/MANUALFC_MASTER_FINAL_ACCEPTANCE_AUDIT.md", REPORT("TASK-3601")],
    SCHEMA_OK + ["Snapshot-ul pre-repair este pastrat separat si imuabil.",
                 "Zero probleme CRITICAL sau MAJOR cunoscute dupa retest.",
                 "Limitarile cross-browser, npm advisory, human learning si field input sunt declarate onest."],
    volume="CONTROL-PLANE", units=4, status="DONE",
    validations=["python scripts/validate_project.py", "python scripts/validate_content.py --strict",
                 "python scripts/validate_gold_standard_v2.py", "python -m pytest -q",
                 "npm.cmd test", "npm.cmd run check", "npm.cmd run build"])
add("TASK-3701", "Global Brand Identity Migration: clipboard/M/football master artwork inlocuieste identitatea shield/crest (DEC-0080)", "CONTROL-PLANE", ["TASK-3601"],
    ["public/brand/manualfc/logo/manualfc-brand-master.png",
     "public/brand/manualfc/logo/logo-assets.json",
     "docs/brand/MANUALFC_BRAND_SYSTEM_V2.md",
     "app/src/components/ManualFCLogo.astro",
     "tests/test_task3701_brand_migration.py", REPORT("TASK-3701")],
    SCHEMA_OK + ["Masterul artwork ramane neschimbat pe disk; toate derivatele sunt crop/resize/format-convert ale aceluiasi master, fara redesenare sau distorsiune.",
                 "Zero referinte de cod ramase catre identitatea shield/crest anterioara (fisiere sterse, verificat prin cautare repo-wide).",
                 "Nu exista varianta light-surface/inversata neoficiala inventata -- prop-ul 'surface' a fost eliminat din ManualFCLogo.astro.",
                 "Tokenurile de design (--color-bg-brand, --color-brand-gold) raman neschimbate -- recolorare nejustificata evitata explicit.",
                 "Header, footer, favicon, manifest.webmanifest, service worker si meta og:image/twitter:image actualizate consecvent catre noile assets.",
                 "QA real de browser (Chrome via CDP, axe-core) pe 5 rute x 4 viewport-uri confirma logo-ul randat corect, 0 regresii introduse de migrare.",
                 "Un defect preexistent, nelegat de brand (overflow 8px si contrast insuficient pe hero-ul homepage-ului) a fost gasit si declarat explicit, nu ascuns si nu reparat in afara scopului acestui task."],
    volume="CONTROL-PLANE", units=3, status="DONE",
    validations=["python scripts/validate_project.py", "python -m pytest -q",
                 "npm.cmd test", "npm.cmd run check", "npm.cmd run build"])
add("TASK-3702", "Git Object Integrity Investigation: corupere loose-object preexistenta gasita in timpul commit-ului TASK-3701, investigata read-only", "CONTROL-PLANE", ["TASK-3701"],
    [REPORT("TASK-3702")],
    SCHEMA_OK + ["Toate cele 11 obiecte corupte identificate prin fsck sunt mapate la path/commit sau la ref-ul de checkpoint intern care le contine.",
                 "Confirmat ca HEAD si toate fisierele curente sunt neafectate (build/teste/status functioneaza normal).",
                 "Nicio operatie de scriere/reparare/rewrite asupra bazei de obiecte Git, multi-pack-index sau refs/codex nu a fost executata.",
                 "Cautare de surse alternative (remote, worktree-uri locale) documentata -- niciuna disponibila -- verdict BLOCKED pentru reparare, nu ascuns."],
    volume="CONTROL-PLANE", units=1, status="DONE",
    validations=["git fsck --full", "git rev-list --objects --all"])
add("TASK-3703", "Post-Brand Visual Debug, Regression Repair & Acceptance: inchide overflow-ul homepage si contrastul 01, audit complet de regresie pe 10 suprafete x 5 viewport-uri", "CONTROL-PLANE", ["TASK-3701", "TASK-3702"],
    ["plans/TASK-3703-post-brand-visual-debug.md",
     "reports/audits/MANUALFC_POST_BRAND_VISUAL_ACCEPTANCE.md", REPORT("TASK-3703")],
    SCHEMA_OK + ["Overflow-ul de ~8px de pe homepage (HomepageHero.astro .approved-hero, index.astro .final-cta) reprodus, cauza-radacina identificata (100vw include scrollbar-ul) si reparat cu tiparul deja stabilit (masurare JS + --scrollbar-w), 0 overflow verificat la 320/390/768/1280/1440.",
                 "Contrastul indicatorului 01 (.proof-index b, culoare --color-border pe fundal --color-bg-main, 1.42:1) reparat la --color-text-muted (4.63:1), token existent, fara culoare noua inventata.",
                 "Doua defecte suplimentare de acelasi tip, gasite in timpul auditului obligatoriu si dovedite preexistente TASK-3701 (git show pe commit-ul 0466ea9): overflow identic pe incepe-aici.astro (.founding-rule) si contrast insuficient pe spatiul-meu (.continue .eyebrow/.continue p) -- reparate cu acelasi tipar minim, nu doar declarate.",
                 "Audit real de browser (Chrome via CDP, axe-core) pe 10 suprafete x 5 viewport-uri = 50 combinatii, toate PASS: 0 overflow, 0 violari Axe, main=1, h1=1, 0 imagini rupte, 0 erori de consola.",
                 "Integritatea activelor de brand verificata programatic: hash-uri SHA-256, dimensiuni, mod, rapoarte de aspect fara bleed -- toate din logo-assets.json confirmate.",
                 "Corupția Git documentata in TASK-3702 ramane neatinsa; o a 12-a instanta a aceleiasi clase de corupere, gasita incidental (git log pe incepe-aici.astro), este doar mentionata, nu reparata."],
    volume="CONTROL-PLANE", units=2, status="DONE",
    validations=["python scripts/validate_project.py", "python scripts/generate_task_registry.py --check",
                 "python scripts/validate_content.py --strict", "python -m pytest -q",
                 "npm.cmd test", "npm.cmd run check", "npm.cmd run build",
                 "python scripts/validate_html_landmarks.py", "python scripts/audit_route_links.py", "git diff --check"])
add("TASK-3704", "Header/footer logo seam repair: --color-bg-brand corectat la culoarea exacta a fundalului artwork-ului master, eliminand efectul de 'sticker' vizibil in jurul logo-ului", "CONTROL-PLANE", ["TASK-3703"],
    ["config/visual-tokens.json", "app/src/styles/tokens.css", "docs/brand/MANUALFC_BRAND_SYSTEM_V2.md", REPORT("TASK-3704")],
    SCHEMA_OK + ["Cauza-radacina dovedita prin esantionare de pixeli, nu presupusa: fundalul header-ului (rgb(13,27,42), tokenul vechi) difera vizibil de fundalul propriu al imaginii logo-ului (rgb(1,10,23)), creand un chenar dreptunghiular vizibil in jurul logo-ului in header si footer.",
                 "--color-bg-brand corectat la #010916 (medie pe un patch de 40x40px din colțul artwork-ului master, nu un singur pixel ghicit), in config/visual-tokens.json (sursa canonica) si app/src/styles/tokens.css.",
                 "Toate literalele hardcodate #0D1B2A care reprezentau acelasi rol semantic (fundal brand) inlocuite cu var(--color-bg-brand): HomepageHero.astro, design-system.astro (swatch-urile din laboratorul de brand), theme-color din BaseLayout.astro, theme_color din manifest.webmanifest.",
                 "--color-text-primary (aceeasi valoare veche, dar rol semantic diferit -- text pe fundal deschis) si liniile decorative ale mingii din HeroBallFlight.astro (culoare de cerneala pe fundal deschis, nelegate de fundalul brand) lasate neschimbate, corect.",
                 "Verificat vizual dupa reparatie (captura de ecran + esantionare de pixeli): 0 tranzitie de culoare la marginea logo-ului in header si footer, la 390px si 1440px.",
                 "0 regresii: pytest 518/518, axe 0 violari pe 4 rute x 2 viewport-uri re-verificate, npm run check/build PASS."],
    volume="CONTROL-PLANE", units=1, status="DONE",
    validations=["python -m pytest -q", "npm.cmd run check", "npm.cmd run build"])
add("TASK-3705", "Header/footer brand lockup rebalansare: inaltimea header-ului si dimensiunile logo-ului aduse la un standard editorial restrans, cu tokenuri CSS reutilizabile", "CONTROL-PLANE", ["TASK-3704"],
    ["app/src/styles/tokens.css", "app/src/components/AppHeader.astro", "app/src/components/AppFooter.astro", REPORT("TASK-3705")],
    SCHEMA_OK + ["Tokenuri CSS reutilizabile adaugate (--brand-logo-header-height:36px, --brand-logo-mobile-height:30px, --brand-logo-footer-width:180px) in tokens.css -- o singura sursa de adevar, nu dimensiuni hardcodate in mai multe fisiere.",
                 "Header desktop: inaltime 86px->72px (masurat real: 73px), logo redimensionat pe inaltime (36px, latime auto ~138px), in intervalul cerut 32-38px.",
                 "Header mobil (<=700px): inaltime 78px->68px (masurat real: 69px), logo 30px inaltime (~115px latime), in intervalul cerut 28-32px.",
                 "Footer: logo de la 260px la 180px latime (var(--brand-logo-footer-width)), in intervalul cerut 160-200px, tagline ramane vizibil (copt in imaginea 'full').",
                 "Confirmat, fara modificare: hero-ul homepage-ului NU contine niciun logo (doar text/imagine) -- cerinta de a nu duplica branding-ul in hero era deja indeplinita.",
                 "Confirmat, fara modificare: artwork-ul mare de brand nu e folosit nicaieri ca sectiune full-width -- folosit doar pentru og:image/twitter:image, conform optiunii preferate din cerinta.",
                 "Verificare vizuala reala (Chrome via CDP) la toate cele 7 viewport-uri cerute (1440/1280/1024/768/430/390/360): header, meniu mobil deschis/inchis, footer desktop/mobil, homepage complet -- toate randate corect, 0 distorsiune, 0 taiere.",
                 "0 regresii: pytest 518/518, npm run check/build PASS, axe 0 violari pe toate cele 7 viewport-uri, 0 overflow orizontal."],
    volume="CONTROL-PLANE", units=1, status="DONE",
    validations=["python -m pytest -q", "npm.cmd run check", "npm.cmd run build",
                 "python scripts/validate_project.py", "python scripts/validate_html_landmarks.py",
                 "python scripts/audit_route_links.py", "git diff --check"])
add("TASK-3711", "P0 Product Stabilization: repararea rutei CTA 'Rezolva pe teren', declararea reala a dependentelor playwright/@axe-core-playwright, SEO tehnic minim (site/canonical/sitemap/robots) si smoke test real de browser+accesibilitate", "CONTROL-PLANE", ["TASK-3705"],
    ["app/src/components/AppHeader.astro", "app/src/components/AppFooter.astro", "app/src/components/HomepageHero.astro",
     "app/src/pages/incepe-aici.astro", "app/src/layouts/BaseLayout.astro", "astro.config.mjs", "public/robots.txt",
     "package.json", "package-lock.json", "tests/web/browser-a11y-smoke.test.js",
     "plans/TASK-3711-p0-product-stabilization.md", REPORT("TASK-3711")],
    SCHEMA_OK + [
        "Cauza radacina a CTA-ului 'Rezolva pe teren' dovedita, nu presupusa: getPrimaryNavigation() intorcea deja ruta reala /rezolva-pe-teren, dar AppHeader.astro filtra pe cheia veche /gold-standard/rapid (item eliminat silentios din nav); AppFooter/HomepageHero/incepe-aici aveau href hardcodat la ruta veche.",
        "Header/footer/hero/onboarding repointate la /rezolva-pe-teren; referintele interne legitime din gold-standard/index.astro si volum/index.astro catre pagina legacy gold-standard/rapid.astro (care exista in continuare si leaga ea insasi inapoi la /rezolva-pe-teren) lasate neschimbate, fara motiv functional de schimbare.",
        "playwright si @axe-core/playwright declarate ca devDependencies reale in package.json, cu package-lock.json actualizat prin npm install normal (nu --no-save, nu editare manuala).",
        "astro.config.mjs are 'site' setat (singurul URL real documentat, manualfc.vercel.app, DEC-0053 -- domeniul de productie propriu ramane o decizie de produs neluata inca) si integrarea @astrojs/sitemap; BaseLayout.astro are canonical/og:url/og:image rezolvate absolut (inlocuind marcajul anterior 'Site URL = unresolved'); public/robots.txt valid, cu Sitemap: catre sitemap-index.xml.",
        "tests/web/browser-a11y-smoke.test.js: Chromium real via Playwright, verifica homepage, exact un main, exact un h1, ruta CTA reparata, si 0 violari axe-core pe 6 pagini critice.",
        "Fresh clone independent din origin (E:/ManualFC-remote-verify-3711): npm install, npm run check, npm test (9/9), pytest (518/518), npm run build (101 pagini, identic), sitemap (100 URL-uri + 404.html = 101), git fsck --full curat, arbore de fisiere urmarite identic byte-cu-byte cu repo-ul canonic (948/948, 0 diferente)."],
    volume="CONTROL-PLANE", units=1, status="DONE",
    validations=["python -m pytest -q", "npm.cmd run check", "npm.cmd run build", "npm.cmd test", "git diff --check"])
add("TASK-3712", "Gold Standard Content Expansion: 10 exercitii noi (EX-0006-EX-0015) si 4 sedinte noi (SES-0003-SES-0006) in aceeasi tema deja validata, fara a doua tema de antrenament", "CONTROL-PLANE", ["TASK-3711"],
    ["data/exercises/exercise-unghiul-de-sprijin-din-spate.json", "data/exercises/exercise-unu-doi-pentru-a-iesi-din-umbra.json",
     "data/exercises/exercise-al-treilea-jucator-de-sprijin.json", "data/exercises/exercise-receptie-sub-presiune-completa.json",
     "data/exercises/exercise-momentul-potrivit-de-plecare.json", "data/exercises/exercise-patru-sprijiniri-o-singura-minge.json",
     "data/exercises/exercise-prima-privire-dupa-recuperare.json", "data/exercises/exercise-sprijin-pe-culoar-lateral.json",
     "data/exercises/exercise-joc-mic-3v3-doua-porti.json", "data/exercises/exercise-joc-mic-5v5-zona-de-finalizare.json",
     "data/sessions/session-sprijin-din-spate-si-combinatie.json", "data/sessions/session-al-treilea-jucator-si-presiune.json",
     "data/sessions/session-recuperare-si-sprijin-lateral.json", "data/sessions/session-transfer-complet-jocuri-variate.json",
     "data/assessments/assessment-sprijin-si-unghi-de-pasa.json", "data/problems/problem-library.json",
     "app/src/lib/content-bridge.ts", "app/src/components/FieldCard.astro",
     "tests/test_task3712_gold_standard_expansion.py", "tests/web/built-routes.test.js",
     "plans/TASK-3712-gold-standard-content-expansion.md", REPORT("TASK-3712")],
    SCHEMA_OK + [
        "10 exercitii noi (EX-0006-EX-0015) si 4 sedinte noi (SES-0003-SES-0006), toate cu theme='sprijin-si-unghi-de-pasa' -- aceeasi tema deja validata, nicio tema noua de antrenament introdusa.",
        "Fiecare exercitiu are toate campurile V2 obligatorii (verificat de scripts/validate_gold_standard_v2.py, 0 erori pe 15 exercitii/6 sedinte): problema, perceptie, decizie, mesaj exact, cele 7 rationale, cand intervii/nu intervii, progresie/regresie, granita dovezii.",
        "assessment-sprijin-si-unghi-de-pasa.json extins cu 3 criterii noi (C6-C8), nu cate unul per exercitiu -- ramane un instrument de teren utilizabil, nu un tabel birocratic de 15 randuri.",
        "problem-library.json intarit pentru PRB-0001,0002,0003,0005,0007,0008; PRB-0005 (assessment_links gol anterior) legat acum corect la ASM-0001 prin EX-0012. PRB-0004/PRB-0006 (organizare defensiva) lasate deliberat orfane -- construirea de exercitii pentru ele ar fi insemnat, de fapt, o a doua tema de antrenament.",
        "Defect real gasit si reparat: app/src/components/FieldCard.astro randa TacticalDiagram necondiționat pentru orice exercitiu, ceea ce oprea complet npm run build imediat ce a aparut un exercitiu (EX-0006) in afara variantelor EX-0001-EX-0005 cunoscute de TacticalDiagram -- reparat cu acelasi tipar hasDiagram/nota onesta deja folosit in exercitii/[id].astro si sedinte/[id]/mod-teren.astro.",
        "content-bridge.ts actualizat (liste hardcodate, nu glob) cu toate cele 15 exercitii si 6 sedinte; build produce 119 pagini (101+18), fara pagini orfane sau linkuri rupte (audit_route_links.py: 0 BROKEN_INTERNAL_REFS).",
        "Verificare reala de browser (Playwright, Chromium) la 1440px si 390px pe 8 pagini noi/afectate: 0 overflow orizontal, main=1/h1=1 peste tot, 0 violari axe.",
        "Fresh clone independent din origin (E:/ManualFC-remote-verify-3712): npm install, npm run check, npm test (9/9), pytest (554/554), npm run build (119 pagini, identic), sitemap (118 URL-uri + 404.html = 119), audit_route_links.py PASS, comportament offline verificat cu browser real, git fsck --full curat, arbore de fisiere urmarite identic byte-cu-byte cu repo-ul canonic (965/965, 0 diferente)."],
    volume="CONTROL-PLANE", units=2, status="DONE",
    validations=["python -m pytest -q", "npm.cmd run check", "npm.cmd run build", "npm.cmd test",
                 "python scripts/validate_content.py --strict", "python scripts/validate_gold_standard_v2.py",
                 "python scripts/audit_route_links.py", "git diff --check"])
add("TASK-3713", "ManualFC Private Pilot Setup: protocol de pilot cu 2-3 antrenori U11 reali, pachet pentru antrenor, format de captura a observatiilor -- pregatire, fara date de teren", "CONTROL-PLANE", ["TASK-3712"],
    ["docs/field-pilot/MANUALFC_PRIVATE_PILOT_PROTOCOL.md", "docs/field-pilot/PRIVATE_PILOT_COACH_PACK.md",
     "docs/field-pilot/PRIVATE_PILOT_OBSERVATION_TEMPLATE.md", "tests/test_task3713_private_pilot.py",
     "plans/TASK-3713-private-pilot-setup.md", REPORT("TASK-3713")],
    SCHEMA_OK + [
        "Protocol complet (MANUALFC_PRIVATE_PILOT_PROTOCOL.md): profil participant si criterii de includere, ipoteze de recrutare, participare informata si limite de confidentialitate, durata (2-4 saptamani, minimum 2 sedinte reale/antrenor), cele 9 scenarii de sarcini obligatorii, conditii mobil/desktop si online/offline, metoda de observare, intrebari de debrief, disciplina RAW OBSERVATION/INTERPRETATION/CONFIDENCE, regula explicita spune-vs-face, criterii de succes/oprire, clasificare de severitate pe 4 niveluri, metoda de prioritizare, si decizia MUST FIX/SHOULD FIX/NOT NOW/IGNORE.",
        "Se raporteaza onest, nu se ascunde: PHASE-23/TASK-2301 (Runda 1, doar SES-0001, un singur antrenor) ramane, la randul ei, neexecutata (FIELD_INPUT_REQUIRED neschimbat de la acel task) -- noul protocol o extinde constient, nu o inlocuieste si nu pretinde ca a rezolvat-o.",
        "Pachet pentru antrenor (PRIVATE_PILOT_COACH_PACK.md): instructiuni printabile/partajabile, fara jurgon de cercetare, cu cele 9 sarcini in forma practica si asigurari explicite de confidentialitate in limbaj simplu.",
        "Format de captura (PRIVATE_PILOT_OBSERVATION_TEMPLATE.md): cate o sectiune per sarcina cu RAW OBSERVATION/INTERPRETATION/CONFIDENCE separate, coduri de-identificate A1/A2/A3, lista de verificare a confidentialitatii inainte de trimitere.",
        "Inspectia jurnalului antrenorului (cod + browser real Playwright la 1440px/390px pe toate cele 11 suprafete cerute) nu a gasit niciun defect de produs care sa necesite reparatie -- 'recents' (revenire la un articol folosit anterior) functioneaza deja prin recordRecent() din CoachActions.astro, 'Spatiul meu' e deja 100% local-first (localStorage, fara cont, fara server), avertismentele de confidentialitate exista deja pe formularele de reflectie si constructie de sedinta. Niciun cod de produs nu a fost modificat -- nu s-a inventat o schimbare doar pentru a avea un diff.",
        "Niciun rezultat, participant, citat sau dovada de teren nu a fost inventat sau simulat -- pilotul nu a fost inca executat; PHASE-23 ramane FIELD_INPUT_REQUIRED.",
        "22 teste noi (tests/test_task3713_private_pilot.py) verifica existenta documentelor, absenta rezultatelor fabricate, respectarea limitelor de confidentialitate, absenta jurgonului de cercetare in pachetul pentru antrenor, si acoperirea tuturor sectiunilor/scenariilor cerute.",
        "Fresh clone independent din origin (E:/ManualFC-remote-verify-3713): npm install, npm run check, npm test (9/9), pytest (576/576), npm run build (119 pagini, neschimbat), audit_route_links.py PASS, comportament offline verificat cu browser real, git fsck --full curat, arbore de fisiere urmarite identic byte-cu-byte cu repo-ul canonic (971/971, 0 diferente)."],
    volume="CONTROL-PLANE", units=1, status="DONE",
    validations=["python -m pytest -q", "npm.cmd run check", "npm.cmd run build", "npm.cmd test",
                 "python scripts/audit_route_links.py", "git diff --check"])
add("TASK-3715", "Redeploy ManualFC from origin/main and Verify the Live Production Deployment -- verdict BLOCKED (fara acces Vercel autentificat), investigat complet, nicio ocolire", "CONTROL-PLANE", ["TASK-3713"],
    [REPORT("TASK-3715"), "plans/TASK-3715-redeploy-and-verify-production.md"],
    SCHEMA_OK + [
        "Acces de deployment verificat exhaustiv si dovedit indisponibil: `vercel whoami` -> Logged out; niciun `.vercel/project.json` in repo; nicio variabila VERCEL_TOKEN/VERCEL_ORG_ID/VERCEL_PROJECT_ID; niciun `auth.json` pentru Vercel CLI pe disc; niciun tool MCP de deployment Vercel inregistrat in sesiune.",
        "Proiectul/URL-ul de productie confirmat din documentatia existenta, fara a inventa un domeniu: `manualfc` (prj_P2o9rzNbCsHraLk5CWVQGozAOZuU), alias `https://manualfc.vercel.app/` (reports/deployments/TASK-2601-vercel-staging.md, DEC-0053).",
        "Stare live curenta verificata direct, cu browser real, fara nicio autentificare Vercel: CTA header/footer/hero live inca `/gold-standard/rapid` (exact defectul reparat de TASK-3711, neajuns inca live); ruta `/gold-standard/exercitii/EX-0006/` (TASK-3712) -> 404 pe live; `/robots.txt` si `/sitemap-index.xml` (TASK-3711) -> 404 pe live; niciun tag canonical/og:url pe homepage live -- dovada directa ca deployment-ul live precede TASK-3711/3712/3713.",
        "Validare locala completa rulata integral, chiar sub blocaj: `npm run check` 0 erori, `npm test` 9/9, `pytest` 576/576, `npm run build` 119 pagini, `audit_route_links.py` 0 linkuri rupte, toate EX-0006-EX-0015/SES-0003-SES-0006 prezente local, CTA local 100% `/rezolva-pe-teren` (0 aparitii `/gold-standard/rapid`), canonical/og:url prezente si corecte local, comportament offline functional local -- dovedeste ce ANUME ar fi trebuit sa fie live, fara a putea publica.",
        "Niciun deployment de substitutie, niciun `vercel login` interactiv incercat, nicio modificare de repository facuta pentru a ocoli blocajul -- conform regulii explicite a taskului.",
        "Niciun cod de produs sau configuratie modificata; working tree ramane curat (doar ExecPlan + raport + guvernanta); local main == origin/main neschimbat pe tot parcursul."],
    volume="CONTROL-PLANE", units=1, status="DONE",
    validations=["npm.cmd run check", "npm.cmd run build", "npm.cmd test", "python -m pytest -q",
                 "python scripts/audit_route_links.py", "git diff --check"])
add("TASK-3716", "Unblock Vercel Deployment and Publish the Validated ManualFC Baseline -- deblocare prin flux OAuth de dispozitiv, deploy de productie reusit, verificare live completa, verdict PASS", "CONTROL-PLANE", ["TASK-3715"],
    [REPORT("TASK-3716"), "plans/TASK-3716-unblock-and-deploy.md"],
    SCHEMA_OK + [
        "Deblocare legitima prin fluxul de dispozitiv OAuth al Vercel CLI (`vercel login` -> URL + cod afisat, confirmat de utilizator in propriul browser) -- calea A explicit autorizata de task; niciun token/parola vazut vreodata de acest proces.",
        "Proiect legat explicit la cel existent, nu creat unul nou: `vercel link --project manualfc --scope berescristi-8889s-projects` (scope obtinut din `vercel teams ls`, nu presupus, dupa ce o presupunere initiala gresita a fost respinsa explicit de CLI). `.vercel/project.json` rezultat: `projectId: prj_P2o9rzNbCsHraLk5CWVQGozAOZuU` -- identic cu ID-ul documentat in TASK-2601.",
        "Validare locala completa inainte de deploy: `npm run check` 0 erori, `npm test` 9/9, `pytest` 576/576, `npm run build` 119 pagini, `audit_route_links.py` 0 linkuri rupte, offline functional local -- rulata la exact `HEAD == origin/main == d2c6c5a399cf245290bb7a1f04f4c7da0763ea22`, tree curat.",
        "Deployment de productie reusit: `vercel --prod --yes` din E:/ManualFC-clean -> `dpl_FEhcEK61vhgJgHh1qoYrzUsih8Cj`, `target: production`, `readyState: READY`, aliasat automat la `https://manualfc.vercel.app`.",
        "Verificare live completa cu browser real, dupa deploy: CTA header/footer/hero live acum `/rezolva-pe-teren` (0 aparitii `/gold-standard/rapid` in pozitii de CTA); toate rutele testate (EX-0006, EX-0010, EX-0015, SES-0003-SES-0006, rezolva-pe-teren, gold-standard, principii, volum, incepe-aici) -> 200; `/robots.txt`/`/sitemap-index.xml`/`/sitemap-0.xml` -> 200, sitemap contine 118 URL-uri inclusiv EX-0015/SES-0006; canonical si og:url prezente si corecte (`https://manualfc.vercel.app/`).",
        "Accesibilitate live: 0 violari axe pe 5 pagini (homepage, Decision Engine, EX-0006, SES-0003, principii), main=1/h1=1 peste tot, focus de tastatura vizibil (outline 3px solid). Responsive: 0 overflow orizontal la 1440px si 390px pe 4 pagini cheie. Offline: service worker activ, homepage si o pagina vizitata anterior raman disponibile offline (200, h1 prezent).",
        "Identitate de deployment: `x-vercel-id`/`x-vercel-cache: HIT`/`age: 88` confirma servirea deployment-ului nou-creat la momentul verificarii; proiectul nu are integrare Git (deploy prin CLI, upload direct), deci nu exista un SHA Git expus de Vercel -- cea mai puternica dovada disponibila e combinatia sursa exacta (HEAD==origin/main, tree curat la upload) + amprenta de continut (toate rutele TASK-3711/3712 prezente simultan, nimic stale ramas).",
        "Niciun cod de produs sau configuratie Vercel modificata; niciun credential expus in log-uri/rapoarte; `.vercel/`/`.env.local` raman negestionate de Git (deja in `.gitignore`); local main == origin/main neschimbat de acest task."],
    volume="CONTROL-PLANE", units=1, status="DONE",
    validations=["npm.cmd run check", "npm.cmd run build", "npm.cmd test", "python -m pytest -q",
                 "python scripts/audit_route_links.py", "git diff --check"])
add("TASK-3714", "Execute the Live ManualFC Private Pilot and Produce the Product Reality Check -- PILOT STATUS = NOT STARTED, verdict BLOCKED (nu exista participanti/sesiuni reale), nicio dovada fabricata", "CONTROL-PLANE", ["TASK-3716"],
    [REPORT("TASK-3714"), "plans/TASK-3714-execute-private-pilot.md"],
    SCHEMA_OK + [
        "Cautare exhaustiva, nu presupunere, a oricarei dovezi reale de pilotare in intregul repository: niciun formular de observatie completat, niciun fisier codificat A1/A2/A3 cu date reale, nimic mai nou decat protocolul (TASK-3713) care ar indica participare reala de antrenor. 0 gasite.",
        "Site de productie confirmat accesibil (`https://manualfc.vercel.app/` -> 200) inainte si dupa investigatie -- blocajul e specific participantilor/sesiunilor reale, nu accesului la produs.",
        "PILOT STATUS declarat explicit: NOT_STARTED. Niciun participant, sesiune, observatie, citat sau constatare nu a fost inventat sau simulat -- regula absoluta a taskului respectata integral.",
        "Nicio automatizare de browser folosita ca substitut pentru comportament real de antrenor -- ar fi constituit exact fabricarea de dovezi interzisa explicit; QA tehnic (deja facut in TASK-3711-TASK-3716) ramane separat de cercetarea comportamentala reala ceruta de acest task.",
        "Validare de regresie completa rulata, chiar fara nicio modificare de cod: `npm run check` 0 erori, `npm test` 9/9, `pytest` 576/576 -- dovedeste ca starea repository-ului ramane solida, gata pentru un pilot real, in asteptarea participantilor.",
        "Niciun Product Reality Check scris -- nu exista dovezi reale de rezumat; scrierea unuia ar fi incalcat regula explicita a taskului.",
        "Actiunea exacta ceruta din partea utilizatorului: recrutarea a 2-3 antrenori reali conform PRIVATE_PILOT_COACH_PACK.md, desfasurarea a minimum 2 sedinte reale per antrenor pe o fereastra de 2-4 saptamani, si returnarea formularelor PRIVATE_PILOT_OBSERVATION_TEMPLATE.md completate -- abia atunci un task viitor poate produce Product Reality Check-ul real."],
    volume="CONTROL-PLANE", units=1, status="DONE",
    validations=["npm.cmd run check", "npm.cmd test", "python -m pytest -q", "git diff --check"])
add("TASK-3718", "Build and Validate the Second Complete ManualFC Training Theme: apararea (presiune si acoperire, tranzitia negativa, protejarea centrului) -- 10 exercitii noi (EX-0016-EX-0025), 4 sedinte noi (SES-0007-SES-0010), 1 evaluare noua (ASM-0002), verdict PASS, pilotarea reala ramane indisponibila", "CONTROL-PLANE", ["TASK-3714"],
    ["data/exercises/exercise-incetineste-nu-ataca-mingea.json", "data/exercises/exercise-unul-incetineste-celalalt-protejeaza.json",
     "data/exercises/exercise-schimba-rolul-cand-mingea-se-muta.json", "data/exercises/exercise-nu-va-eliminati-amandoi.json",
     "data/exercises/exercise-al-doilea-aparator-acopera-drumul.json", "data/exercises/exercise-primele-doua-secunde-dupa-pierdere.json",
     "data/exercises/exercise-cine-e-aproape-cine-protejeaza-centrul.json", "data/exercises/exercise-recupereaza-forma-nu-doar-mingea.json",
     "data/exercises/exercise-joc-mic-4v4-observare-defensiva.json", "data/exercises/exercise-joc-mic-6v6-zona-de-protejat.json",
     "data/sessions/session-incetinire-si-schimb-de-rol.json", "data/sessions/session-coordonare-defensiva-2v2.json",
     "data/sessions/session-tranzitie-negativa-si-echipa.json", "data/sessions/session-transfer-defensiv-complet.json",
     "data/assessments/assessment-apararea-presiune-si-acoperire.json", "data/problems/problem-library.json",
     "app/src/lib/content-bridge.ts", "app/src/lib/discovery-index.ts", "app/src/lib/problem-library.ts",
     "app/src/pages/aparare/index.astro", "app/src/pages/gold-standard/index.astro",
     "app/src/pages/gold-standard/configurator.astro", "app/src/pages/gold-standard/fise-de-teren.astro",
     "app/src/pages/gold-standard/exercitii/[id].astro", "app/src/pages/gold-standard/sedinte/[id].astro",
     "app/src/pages/gold-standard/evaluare/[id].astro", "app/src/pages/spatiul-meu/reflectie.astro",
     "tests/test_task3718_second_training_theme.py", "tests/test_task3712_gold_standard_expansion.py",
     "tests/web/built-routes.test.js", "plans/TASK-3718-second-training-theme.md", REPORT("TASK-3718")],
    SCHEMA_OK + [
        "Tema aleasa nu e arbitrara: 3 candidati evaluati explicit pe 8 criterii (relevanta pentru antrenor, adiacenta pedagogica, distinctie fata de 'Sprijinul si unghiul de pasa', profunzime de continut disponibila, transferabilitate in joc reprezentativ, efort de schema/implementare, risc de duplicare, capacitate de a construi o tema completa acum) in plans/TASK-3718-second-training-theme.md -- 'Apararea: presiune si acoperire' aleasa pentru ca era singura cu infrastructura deja evidentiata (PRB-0004/PRB-0006 orfane + 3 principii canonice cu evidence_claim_ids reale), evitand fabricarea de cercetare noua.",
        "10 exercitii noi (EX-0016-EX-0025, theme='apararea-presiune-si-acoperire') si 4 sedinte noi (SES-0007-SES-0010), toate cu profunzimea completa V2 (verificat de scripts/validate_gold_standard_v2.py, 0 erori pe 25 exercitii/10 sedinte): problema, perceptie, decizie, mesaj exact, cele 7 rationale, cand intervii/nu intervii, progresie/regresie, granita dovezii.",
        "ASM-0002 (5 criterii) creata; PRB-0004 si PRB-0006 (lasate deliberat orfane de TASK-3712) intarite acum cu related_exercises/related_sessions/assessment_links reale -- exact tema pentru care fusesera rezervate.",
        "Limitare arhitecturala reala gasita si generalizata minimal: getGoldStandardAssessment() era hardcodat la o singura evaluare, consumat fara parametri in 6 locuri. Generalizat compatibil retroactiv (parametru optional cu valoare implicita 'ASM-0001' plus getGoldStandardAssessments() noua); 3 consumatori care presupuneau o singura evaluare globala reparati (gold-standard/sedinte/[id].astro, gold-standard/evaluare/[id].astro, spatiul-meu/reflectie.astro) si assessmentIds din validateProblemGraph() actualizat.",
        "Rutele de detaliu (exercitii/sedinte/evaluare) raman comune la /gold-standard/... pentru ambele teme, ca sa nu rupa URL-uri live; gold-standard/index.astro, fise-de-teren.astro si configurator.astro filtrate explicit la theme==='sprijin-si-unghi-de-pasa' (camp text deja existent, nicio schimbare de schema) ca sa nu absoarba tacit continutul temei 2; navigarea prev/next si breadcrumb din exercitii/[id].astro scopate la aceeasi tema. Pagina noua /aparare/ e singura suprafata noua de navigare, cu legaturi reciproce catre /gold-standard/, /principii/ si /rezolva-pe-teren/.",
        "Fisierele canonice ale temei 1 raman identice byte-cu-byte (git diff curat pe exercise-recunoasterea-umbrei-defensive.json, session-introducere.json, assessment-sprijin-si-unghi-de-pasa.json etc.) -- nicio corupere a Gold Standard-ului existent.",
        "21 teste noi (tests/test_task3718_second_training_theme.py) plus tests/test_task3712_gold_standard_expansion.py actualizat (asertiunea 'PRB-0004/PRB-0006 raman neatinse' devenea falsa prin design, nu o regresie -- actualizata sa reflecte ca TASK-3718 construieste exact tema pentru care fusesera rezervate).",
        "Verificare reala de browser (Playwright, Chromium, cu @axe-core/playwright) la 1440px si 390px pe 6 pagini (inclusiv /aparare/, /gold-standard/evaluare/ASM-0002/, /gold-standard/exercitii/EX-0020/, /gold-standard/sedinte/SES-0009/): 12/12 verificari trecute, 0 violari axe, 0 erori de consola.",
        "npm run build produce 139 pagini (119+20: 10 exercitii + 4 sedinte x2 rute + 1 evaluare + 1 pagina de tema); tests/web/built-routes.test.js actualizat de la 119 la 139 cu justificare explicita in comentariu; sitemap contine toate rutele noi.",
        "Nicio pretentie de validare de teren: raportul si continutul noii teme afirma explicit ca pilotarea reala (TASK-3714) ramane BLOCKED si intentionat sarita pentru aceasta faza -- nicio afirmatie din /aparare/ sau ASM-0002 nu presupune coachi reali."],
    volume="CONTROL-PLANE", units=2, status="DONE",
    validations=["python -m pytest -q", "npm.cmd run check", "npm.cmd run build", "npm.cmd test",
                 "python scripts/validate_content.py --strict", "python scripts/validate_gold_standard_v2.py",
                 "git diff --check"])
add("TASK-3719", "Build the Communication Scripts Content Pillar: 26 scripturi noi (SCR-0001-SCR-0026) in toate cele 14 categorii cerute, legate real la ambele teme si la motorul de decizie, verdict PASS, pilotarea reala ramane indisponibila", "CONTROL-PLANE", ["TASK-3718"],
    ["data/communication-scripts/script-tacere-activa-inainte-de-interventie.json",
     "data/communication-scripts/script-un-singur-lucru-per-interventie.json",
     "data/communication-scripts/script-priveste-inainte-sa-vina-mingea.json",
     "data/communication-scripts/script-orienteaza-te-spre-spatiul-liber.json",
     "data/communication-scripts/script-iesi-din-umbra-adversarului.json",
     "data/communication-scripts/script-nu-va-adunati-in-aceeasi-zona.json",
     "data/communication-scripts/script-nu-ramane-pe-loc-dupa-ce-ai-pasat.json",
     "data/communication-scripts/script-primele-doua-secunde-dupa-pierdere.json",
     "data/communication-scripts/script-cine-e-aproape-cine-protejeaza-centrul.json",
     "data/communication-scripts/script-prima-privire-nu-prima-pasa-inapoi.json",
     "data/communication-scripts/script-ai-castigat-mingea-ce-vezi-inainte.json",
     "data/communication-scripts/script-unul-incetineste-celalalt-protejeaza.json",
     "data/communication-scripts/script-nu-va-eliminati-amandoi-cu-aceeasi-actiune.json",
     "data/communication-scripts/script-ce-vezi-inainte-sa-alegi.json",
     "data/communication-scripts/script-nu-exista-o-singura-solutie-corecta.json",
     "data/communication-scripts/script-greseala-e-informatie-nu-verdict.json",
     "data/communication-scripts/script-lauda-efortul-nu-doar-rezultatul.json",
     "data/communication-scripts/script-ce-ai-observat-azi.json",
     "data/communication-scripts/script-unde-ai-mai-vazut-asta-in-joc.json",
     "data/communication-scripts/script-esti-frustrat-hai-sa-respiram-o-secunda.json",
     "data/communication-scripts/script-doi-copii-se-cearta-pe-minge.json",
     "data/communication-scripts/script-toata-lumea-atinge-mingea.json",
     "data/communication-scripts/script-nu-eticheta-copilul-care-greseste-des.json",
     "data/communication-scripts/script-de-ce-am-schimbat-regula.json",
     "data/communication-scripts/script-ce-luati-cu-voi-la-meci.json",
     "data/communication-scripts/script-inchidem-cu-un-singur-lucru.json",
     "schemas/communication-script.schema.json", "scripts/validate_communication_scripts.py",
     "app/src/lib/content-bridge.ts", "app/src/lib/discovery-index.ts", "app/src/lib/coach-state.ts",
     "app/src/components/CoachActions.astro",
     "app/src/pages/scripturi/index.astro", "app/src/pages/scripturi/[id].astro",
     "app/src/pages/gold-standard/exercitii/[id].astro", "app/src/pages/gold-standard/sedinte/[id].astro",
     "app/src/pages/principii/[slug].astro",
     "tests/test_task3719_communication_scripts.py", "tests/web/built-routes.test.js",
     "plans/TASK-3719-communication-scripts-pillar.md", REPORT("TASK-3719")],
    SCHEMA_OK + [
        "Pilon ales explicit dintre cei 3 pilonii goi (studii de caz/scripturi de comunicare/planuri de sezon) semnalati de roadmap-ul canonic (Phase 5) -- utilizatorul autorizeaza construirea acum, fara dovezi de pilotare (TASK-3714 ramane BLOCKED), la fel ca la TASK-3718 pentru tema a doua.",
        "26 scripturi noi (SCR-0001-SCR-0026), cate 1-2 per categorie, acoperind toate cele 14 categorii cerute explicit (observare inainte de corectie, receptie si scanare, sprijin si unghiuri de pasa, miscare dupa pasa, tranzitiile la pierderea/castigarea mingii, cooperare defensiva, decizie sub presiune, greseala ca informatie, reflectie si autoevaluare, conflict/frustrare, incluziune/echitate, explicarea constrangerilor, inchiderea sedintei/transfer).",
        "Schema communication-script.schema.json (schelet neutilizat, 5 proprietati, 0 documente reale inainte de acest task) completata la ~25 campuri, modelata pe message-foundation.schema.json (de asemenea neutilizat ca document de sine statator) -- nu inventata de la zero. Reutilizarea numelor de campuri (child_wording, rationales cu exact 7 dimensiuni) declanseaza automat validatorul FAIL_CLOSED de pedagogie deja existent in validate_content.py, fara cod nou.",
        "Verificare manuala a textului complet al fiecarui claim citat, nu doar cautare de cuvinte cheie: 3 claim-uri gasite initial prin cautare (CLM-0054/0056/0057) s-au dovedit, la citire integrala, intrari auto-corective care declara ca afirmatia initiala era fabricata/nepotrivit atribuita -- nu au fost citate; folosite in schimb claim-urile reale corespunzatoare.",
        "Validator nou dedicat (scripts/validate_communication_scripts.py) -- verifica rezolvarea reala a fiecarui principle_id/related_problem_id/related_exercise_id/related_session_id/source_claim_id, necesar pentru ca validatorul generic nu poate verifica principle_ids (format principle.<slug>, nu se potriveste modelului PREFIX-XXXX).",
        "content-bridge.ts extins cu getCommunicationScripts()/getCommunicationScript(id)/getScriptsForExercise/Session/Principle, toate FAIL_CLOSED; CanonicalKind (coach-state.ts) extins cu 'script' pentru salvare/favorite/recente local-first, fara infrastructura noua.",
        "Doua trasee de descoperire reale: /scripturi/ (filtrare pe 14 categorii + cautare text) si blocuri contextuale 'Scripturi de comunicare relevante' pe exercitii/sedinte/principii, generate din legaturi reale (nu camp de tema denormalizat); indexare completa in cautarea unificata.",
        "Scripturile leaga real continut din ambele teme (EX-0001-0015 tema 1, EX-0016-0025 tema 2) si toate cele 8 probleme din motorul de decizie -- verificat programatic.",
        "16 teste noi (tests/test_task3719_communication_scripts.py); niciun fisier existent din data/exercises, data/sessions, data/assessments, data/problems, data/principles modificat (git diff curat).",
        "Verificare reala de browser (Playwright, Chromium, @axe-core/playwright) la 1440px si 390px pe 7 pagini: 14/14 PASS, 0 violari axe, 0 erori de consola, confirmat ca blocurile de scripturi relevante randeaza legaturi reale.",
        "npm run build produce 166 pagini (139+27: 26 pagini de script + 1 index); tests/web/built-routes.test.js actualizat de la 139 la 166 cu justificare explicita.",
        "Nicio pretentie de validare de teren: raportul si continutul pilonului afirma explicit ca pilotarea reala (TASK-3714) ramane BLOCKED si intentionat sarita pentru aceasta faza."],
    volume="CONTROL-PLANE", units=2, status="DONE",
    validations=["python -m pytest -q", "npm.cmd run check", "npm.cmd run build", "npm.cmd test",
                 "python scripts/validate_content.py --strict", "python scripts/validate_communication_scripts.py",
                 "git diff --check"])
add("TASK-3720", "Build the Season Planning Content Pillar: 4 planuri de sezon (PLAN-0001-PLAN-0004) cu 8 blocuri si 16 microcicluri, progresie pedagogica reala legata la ambele teme, scripturi si motorul de decizie, verdict PASS, pilotarea reala ramane indisponibila", "CONTROL-PLANE", ["TASK-3719"],
    ["data/curriculum/curriculum-traseul-de-baza.json", "data/curriculum/curriculum-aprofundare-sprijin.json",
     "data/curriculum/curriculum-aprofundare-aparare.json", "data/curriculum/curriculum-integrare-completa.json",
     "data/season-plans/season-plan-traseul-de-baza.json", "data/season-plans/season-plan-aprofundare-sprijin.json",
     "data/season-plans/season-plan-aprofundare-aparare.json", "data/season-plans/season-plan-integrare-completa.json",
     "schemas/curriculum.schema.json", "schemas/season-plan.schema.json", "scripts/validate_season_plans.py",
     "app/src/lib/content-bridge.ts", "app/src/lib/discovery-index.ts", "app/src/lib/coach-state.ts",
     "app/src/components/CoachActions.astro",
     "app/src/pages/planuri-de-sezon/index.astro", "app/src/pages/planuri-de-sezon/[id].astro",
     "app/src/pages/rezolva-pe-teren/[slug].astro", "app/src/pages/gold-standard/index.astro",
     "app/src/pages/aparare/index.astro", "app/src/pages/principii/[slug].astro",
     "app/src/pages/gold-standard/exercitii/[id].astro", "app/src/pages/gold-standard/sedinte/[id].astro",
     "app/src/pages/scripturi/[id].astro",
     "tests/test_task3720_season_plans.py", "tests/web/built-routes.test.js",
     "plans/TASK-3720-season-planning-pillar.md", REPORT("TASK-3720")],
    SCHEMA_OK + [
        "Al patrulea pilon de continut ManualFC, autorizat explicit de utilizator fara dovezi de pilotare (TASK-3714 ramane BLOCKED), la fel ca la TASK-3718/TASK-3719 -- de data asta pentru planificarea de sezon, ca sa dea unui antrenor o progresie coerenta pe mai multe saptamani, nu un calendar generic.",
        "Ambele scheme necesare (curriculum.schema.json tip CUR-XXXX/BLK-XXXX, season-plan.schema.json tip PLAN-XXXX/MIC-XXXX) existau deja ca schelete complet neutilizate, cu relatia de compozitie deja corecta (PLAN -> curriculum_ids -> CUR -> blocks) -- completate, nu reproiectate, de la 5-6 proprietati la ~19-26 campuri pedagogice pe nivel.",
        "4 curricula (8 blocuri) si 4 planuri de sezon (16 microcicluri): traseul de baza pentru un grup nou, doua trasee de aprofundare (cate unul per tema de antrenament), si un traseu de integrare completa -- fiecare cu context al problemei, progresie perceptiv-decizionala, criterii de progres/regres, reguli de adaptare, si semnale explicite de continuare/ajustare/incetinire/abandon.",
        "Evidenta despre periodizare (CLM-0366-CLM-0373), deja inregistrata dar neexploatata pana acum, verificata prin citire completa: periodizarea pe blocuri/traditionala e validata aproape exclusiv pe adulti de elita, nu pe dezvoltare juvenila; modelul Cote plaseaza 10-11 ani in anii de esantionare (joc variat, nu specializare). Decizie explicita: pilonul se declara planificare pedagogica, nu periodizare sportiva -- fiecare din cele 4 planuri contine aceasta declaratie explicit in evidence_boundary, verificat programatic.",
        "Referintele EX-/SES-/SCR-/CUR- (format PREFIX-XXXX) sunt validate generic de validate_content.py la orice adancime din document; principle_ids (format cu punct) si duplicatele BLK-/MIC- (imbricate, neindexate generic) au cerut un validator dedicat nou (scripts/validate_season_plans.py).",
        "content-bridge.ts extins cu getCurricula/getSeasonPlans/getSeasonPlan/getCurriculaForPlan si 5 functii de surfacing incrucisat (getSeasonPlansForProblem/Exercise/Session/Principle/Script/Theme), toate FAIL_CLOSED; CanonicalKind extins cu 'season-plan' pentru salvare/favorite local-first.",
        "Doua trasee de descoperire: /planuri-de-sezon/ (navigare pe progresie: pornire -> aprofundare -> integrare, nu calendar filtrabil) si blocuri contextuale 'Plan de sezon relevant' pe 6 tipuri de pagini (probleme, ambele teme, principii, exercitii, sedinte, scripturi), toate din legaturi reale.",
        "Planurile leaga real continut din ambele teme (EX-0001-0015 tema 1, EX-0016-0025 tema 2), din motorul de decizie si din biblioteca de scripturi -- verificat programatic.",
        "23 teste noi (tests/test_task3720_season_plans.py); niciun fisier existent din data/exercises, data/sessions, data/assessments, data/problems, data/principles, data/communication-scripts modificat (git diff curat).",
        "Verificare reala de browser (Playwright, Chromium, @axe-core/playwright) la 1440px si 390px pe 10 pagini: 20/20 PASS, 0 violari axe, 0 erori de consola, confirmat ca toate cele 6 blocuri de plan relevant randeaza legaturi reale.",
        "npm run build produce 171 pagini (166+5: 4 pagini de plan + 1 index); tests/web/built-routes.test.js actualizat de la 166 la 171 cu justificare explicita.",
        "Nicio pretentie de validare de teren: raportul si continutul pilonului afirma explicit ca pilotarea reala (TASK-3714) ramane BLOCKED si intentionat sarita pentru aceasta faza; planurile sunt sinteze profesionale de secventiere, nu garantie de dezvoltare a jucatorului."],
    volume="CONTROL-PLANE", units=2, status="DONE",
    validations=["python -m pytest -q", "npm.cmd run check", "npm.cmd run build", "npm.cmd test",
                 "python scripts/validate_content.py --strict", "python scripts/validate_season_plans.py",
                 "git diff --check"])
add("TASK-3721", "Integrate the coach workflow across all four content systems (teme/metodologie, exercitii/sedinte, scripturi de comunicare, planuri de sezon) intr-un singur traseu coerent problema -> principiu -> exercitiu/sedinta -> script -> plan de sezon -> reflectie -> salvat/continuat, verdict PASS, pilotarea reala ramane indisponibila", "CONTROL-PLANE", ["TASK-3720"],
    ["app/src/lib/content-bridge.ts", "app/src/lib/problem-library.ts", "app/src/lib/coach-state.ts",
     "app/src/components/AppHeader.astro", "app/src/components/AppFooter.astro",
     "app/src/pages/index.astro", "app/src/pages/incepe-aici.astro", "app/src/pages/cauta.astro",
     "app/src/pages/rezolva-pe-teren/[slug].astro", "app/src/pages/gold-standard/exercitii/[id].astro",
     "app/src/pages/gold-standard/sedinte/[id].astro", "app/src/pages/principii/[slug].astro",
     "app/src/pages/planuri-de-sezon/[id].astro", "app/src/pages/spatiul-meu/index.astro",
     "tests/test_task3721_workflow_integration.py", "tests/test_task2703_ia_v2.py",
     "plans/TASK-3721-coach-workflow-integration.md", REPORT("TASK-3721")],
    SCHEMA_OK + [
        "Nu s-a construit un al cincilea sistem de continut, ci s-au reparat tranzitiile reale dintre cele patru deja existente: mapare directa a jurnalului de lucru al antrenorului (citire a ~12 fisiere sursa, nu presupuneri) a gasit navigare cap/footer divergenta, pagini de exercitiu/sedinta/principiu fara legatura inapoi la problema, pagina de problema fara scriptul sau principiul asociat, unealta de reflectie neconectata din nicio pagina, si filtre de cautare care excludeau tacit scripturi/planuri fara metadate de efectiv/durata.",
        "Navigare unificata: header si footer randeaza acum din aceeasi getPrimaryNavigation() (content-bridge.ts), fiecare cu propria harta de etichete/filtrare, eliminand cele doua liste hardcodate divergente semnalate explicit ca risc in cerinta (\"duplicate discovery paths\").",
        "Legaturi noi de continut invers, toate peste campuri relationale deja declarate in date (related_principles/related_exercises/related_sessions/related_problem_ids), niciodata un motor de scor/popularitate nou: getProblemsForExercise/Session/Principle (problem-library.ts, nou) si getScriptsForProblem (content-bridge.ts, nou); pagina de problema afiseaza acum principiul din spate (rezolvare FAIL_CLOSED) si scripturile relevante.",
        "Tranzitie reala reparata: unealta de reflectie (spatiul-meu/reflectie) accepta deja ?sesiune=, dar nimic nu trimitea spre ea. Adaugat CTA de reflectie pe pagina canonica de sedinta si pe fiecare microciclu dintr-un plan de sezon (catre prima sa sedinta).",
        "cauta.astro excludea tacit scripturile/planurile fara efectiv/durata din filtrele Efectiv/Timp; logica de facet corectata sa trateze absenta unui facet ca fiind neaplicabila, nu ca esec de potrivire; etichete de tip lizibile adaugate pentru toate cele 8 tipuri de descoperire.",
        "Spatiul meu: listele de salvate/favorite/recente afiseaza acum o eticheta de tip (CANONICAL_KIND_LABELS, coach-state.ts, nou) pentru fiecare intrare; toate cele cinci stari goale rescrise sa numeasca actiunea concreta care le umple, nu doar absenta continutului -- fara cont, server sau date personale introduse.",
        "Acasa si incepe-aici (onboarding) ofereau doar doua moduri de intrare (invata / rezolva pe teren); planificarea de sezon era accesibila doar din navigare. Adaugat un al treilea mod/intrare catre planuri-de-sezon pe ambele pagini.",
        "29 teste noi (tests/test_task3721_workflow_integration.py), plus 1 test existent (test_task2703_ia_v2.py) actualizat dupa unificarea navigarii footer-ului (schimbare arhitecturala intentionata, nu regresie); niciun continut existent de teme/scripturi/planuri de sezon modificat inutil (git diff limitat la 15 fisiere sursa + 2 fisiere noi).",
        "Verificare reala de browser (Playwright, Chromium, @axe-core/playwright) la 1440px si 390px pe 10 pagini cheie: 20/20 PASS, 0 violari axe, 0 erori de consola, 0 depasire orizontala -- inclusiv navigarea extinsa la 10 elemente in header la 1440px.",
        "npm run build produce tot 171 pagini (nicio ruta noua adaugata in acest task, doar legaturi si continut in paginile existente); sitemap 170 URL-uri + 404.",
        "Nicio pretentie de validare de teren: nici raportul, nici continutul modificat nu afirma ca pilotarea reala a avut loc; TASK-3714 ramane BLOCKED si este mentionat explicit in raport."],
    volume="CONTROL-PLANE", units=2, status="DONE",
    validations=["python -m pytest -q", "npm.cmd run check", "npm.cmd run build", "npm.cmd test",
                 "python scripts/validate_content.py --strict", "python scripts/validate_season_plans.py",
                 "python scripts/validate_communication_scripts.py", "python scripts/validate_gold_standard_v2.py",
                 "git diff --check"])
add("TASK-2717", "Wave-1 browser acceptance, Preview si baseline", "PHASE-27", ["TASK-2704"],
    ["plans/TASK-2717-wave1-acceptance.md", "reports/audits/MANUALFC_WAVE1_BROWSER_ACCEPTANCE.md", REPORT("TASK-2717")],
    SCHEMA_OK + [
        "Candidatul este un commit exact, curat, publicat numai ca Vercel Preview.",
        "Fluxurile critice sunt verificate browser-first pe Preview la 1440/1280/768/390.",
        "Baseline-ul Wave-1 este inghetat numai dupa PASS; orice defect blocant activeaza repararea conditionala."
    ], volume="PREMIUM-WAVE-1", units=3, status="IN_PROGRESS",
    validations=["python scripts/validate_content.py --strict", "python scripts/validate_project.py",
                 "python scripts/generate_task_registry.py --check", "python -m unittest discover -s tests -p \"test_*.py\"",
                 "npm.cmd run check", "npm.cmd run build"])


def materialize() -> dict:
    for task in TASKS:
        if task["task_id"] in web_sequence:
            task["dependencies"], task["title"] = web_sequence[task["task_id"]]
            task["migration_disposition"] = "MOVE_EARLIER"
            for criterion in ("Accesibilitatea web este obligatorie.", "Orice situație dinamică are fallback PDF."):
                if criterion not in task["acceptance_criteria"]:
                    task["acceptance_criteria"].append(criterion)
        if task["title"].startswith("Capitol —"):
            task["migration_disposition"] = "SPLIT"
            criterion = "Producția, auditul pedagogic și auditul editorial rămân verificări distincte."
            if criterion not in task["acceptance_criteria"]:
                task["acceptance_criteria"].append(criterion)
        if task["task_id"] in {"TASK-1401", "TASK-1402", "TASK-1403", "TASK-1404"}:
            task["migration_disposition"] = "REPLACE"
        if task["task_id"].startswith("TASK-17"):
            task["migration_disposition"] = "MOVE_LATER"
    # Ponderile celor șase taskuri închise înaintea pivotului rămân fixe; astfel
    # migrarea nu micșorează artificial progresul deja validat.
    locked = {"TASK-0001": 547, "TASK-0002": 137, "TASK-0101": 410,
              "TASK-0102": 274, "TASK-0103": 547, "TASK-0104": 547}
    unlocked = [task for task in TASKS if task["task_id"] not in locked]
    unlocked_units = sum(task["weight_units"] for task in unlocked)
    remaining = 100_000 - sum(locked.values())
    allocated = 0
    for task in TASKS:
        if task["task_id"] in locked:
            milli = locked[task["task_id"]]
        elif task is unlocked[-1]:
            milli = remaining - allocated
        else:
            milli = round(task["weight_units"] * remaining / unlocked_units)
            allocated += milli
        task.pop("weight_units", None)
        task["weight_percent"] = milli / 1000
        if task["task_id"] == "TASK-0001":
            task["started_at"] = "2026-07-30T00:00:00+03:00"
            task["completed_at"] = "2026-07-30T00:45:00+03:00"
        if task["task_id"] == "TASK-0002":
            task["started_at"] = "2026-07-30T01:00:00+03:00"
            task["completed_at"] = "2026-07-30T01:20:00+03:00"
        if task["task_id"] == "TASK-0101":
            task["status"] = "DONE"
            task["started_at"] = "2026-07-30T02:00:00+03:00"
            task["completed_at"] = "2026-07-30T03:00:00+03:00"
        if task["task_id"] == "TASK-0102":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-07-30T04:00:00+03:00"
            task["completed_at"] = "2026-07-30T05:30:00+03:00"
        if task["task_id"] == "TASK-0103":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-07-30T06:00:00+03:00"
            task["completed_at"] = "2026-07-30T08:30:00+03:00"
        if task["task_id"] == "TASK-0104":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-07-30T09:00:00+03:00"
            task["completed_at"] = "2026-07-30T14:00:00+03:00"
        if task["task_id"] == "TASK-0003":
            task["attempts"] = 1
            task["started_at"] = "2026-07-31T08:00:00+03:00"
            task["completed_at"] = "2026-07-31T12:00:00+03:00"
        if task["task_id"] == "TASK-0004":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-09T12:14:30+03:00"
            task["completed_at"] = "2026-08-09T12:15:00+03:00"
        if task["task_id"] == "TASK-0401":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-09T12:30:00+03:00"
            task["completed_at"] = "2026-08-09T12:35:00+03:00"
        if task["task_id"] == "TASK-0302":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-09T12:45:00+03:00"
            task["completed_at"] = "2026-08-09T13:00:00+03:00"
        if task["task_id"] == "TASK-0201":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-09T13:05:00+03:00"
            task["completed_at"] = "2026-08-09T13:10:00+03:00"
        if task["task_id"] == "TASK-0402":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-09T13:15:00+03:00"
            task["completed_at"] = "2026-08-09T13:25:00+03:00"
        if task["task_id"] == "TASK-0111":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-09T13:30:00+03:00"
            task["completed_at"] = "2026-08-09T13:35:00+03:00"
        if task["task_id"] == "TASK-0202":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-09T13:36:00+03:00"
            task["completed_at"] = "2026-08-09T13:40:00+03:00"
        if task["task_id"] == "TASK-0501":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-09T13:42:00+03:00"
            task["completed_at"] = "2026-08-09T13:50:00+03:00"
        if task["task_id"] == "TASK-0502":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-09T13:55:00+03:00"
            task["completed_at"] = "2026-08-09T14:02:00+03:00"
        if task["task_id"] == "TASK-0503":
            task["status"] = "DONE"
            task["priority"] = "CRITICAL"
            task["attempts"] = 1
            task["started_at"] = "2026-08-09T22:40:00+03:00"
            task["completed_at"] = "2026-08-09T23:10:00+03:00"
        if task["task_id"] == "TASK-0504":
            task["status"] = "DONE"
            task["priority"] = "CRITICAL"
            task["attempts"] = 1
            task["started_at"] = "2026-08-09T23:15:00+03:00"
            task["completed_at"] = "2026-08-09T23:45:00+03:00"
        if task["task_id"] == "TASK-0505":
            task["status"] = "DONE"
            task["priority"] = "CRITICAL"
            task["attempts"] = 1
            task["started_at"] = "2026-08-09T23:50:00+03:00"
            task["completed_at"] = "2026-08-10T00:20:00+03:00"
        if task["task_id"] == "TASK-0506":
            task["status"] = "DONE"
            task["priority"] = "CRITICAL"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T00:25:00+03:00"
            task["completed_at"] = "2026-08-10T00:45:00+03:00"
        if task["task_id"] == "TASK-0507":
            task["status"] = "DONE"
            task["priority"] = "CRITICAL"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T00:50:00+03:00"
            task["completed_at"] = "2026-08-10T01:20:00+03:00"
        if task["task_id"] == "TASK-0601":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T09:00:00+03:00"
            task["completed_at"] = "2026-08-10T10:05:00+03:00"
        if task["task_id"] == "TASK-0602":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T10:20:00+03:00"
            task["completed_at"] = "2026-08-10T11:10:00+03:00"
        if task["task_id"] == "TASK-0603":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T11:20:00+03:00"
            task["completed_at"] = "2026-08-10T12:10:00+03:00"
        if task["task_id"] == "TASK-0604":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T12:20:00+03:00"
            task["completed_at"] = "2026-08-10T13:10:00+03:00"
        if task["task_id"] == "TASK-0605":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T13:20:00+03:00"
            task["completed_at"] = "2026-08-10T14:10:00+03:00"
        if task["task_id"] == "TASK-0606":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T16:10:00+03:00"
            task["completed_at"] = "2026-08-10T17:00:00+03:00"
        if task["task_id"] == "TASK-0607":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T17:05:00+03:00"
            task["completed_at"] = "2026-08-10T18:00:00+03:00"
        if task["task_id"] == "TASK-0608":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T18:05:00+03:00"
            task["completed_at"] = "2026-08-10T19:00:00+03:00"
        if task["task_id"] == "TASK-0609":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T19:05:00+03:00"
            task["completed_at"] = "2026-08-10T19:35:00+03:00"
        if task["task_id"] == "TASK-0610":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T19:40:00+03:00"
            task["completed_at"] = "2026-08-10T20:25:00+03:00"
        if task["task_id"] == "TASK-0701":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T20:30:00+03:00"
            task["completed_at"] = "2026-08-10T21:00:00+03:00"
        if task["task_id"] == "TASK-0702":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T21:05:00+03:00"
            task["completed_at"] = "2026-08-10T21:35:00+03:00"
        if task["task_id"] == "TASK-0703":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T21:40:00+03:00"
            task["completed_at"] = "2026-08-10T22:10:00+03:00"
        if task["task_id"] == "TASK-0704":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T22:15:00+03:00"
            task["completed_at"] = "2026-08-10T22:45:00+03:00"
        if task["task_id"] == "TASK-0705":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T22:50:00+03:00"
            task["completed_at"] = "2026-08-10T23:20:00+03:00"
        if task["task_id"] == "TASK-0706":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-10T23:25:00+03:00"
            task["completed_at"] = "2026-08-10T23:55:00+03:00"
        if task["task_id"] == "TASK-0707":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-11T00:00:00+03:00"
            task["completed_at"] = "2026-08-11T00:30:00+03:00"
        if task["task_id"] == "TASK-0708":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-11T00:35:00+03:00"
            task["completed_at"] = "2026-08-11T01:15:00+03:00"
        if task["task_id"] == "TASK-0801":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-11T01:20:00+03:00"
            task["completed_at"] = "2026-08-11T01:50:00+03:00"
        if task["task_id"] == "TASK-0802":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-11T01:55:00+03:00"
            task["completed_at"] = "2026-08-11T02:25:00+03:00"
        if task["task_id"] == "TASK-0803":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-11T02:30:00+03:00"
            task["completed_at"] = "2026-08-11T03:00:00+03:00"
        if task["task_id"] == "TASK-0804":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-11T03:05:00+03:00"
            task["completed_at"] = "2026-08-11T03:35:00+03:00"
        if task["task_id"] == "TASK-0805":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-11T03:40:00+03:00"
            task["completed_at"] = "2026-08-11T04:10:00+03:00"
        if task["task_id"] == "TASK-0806":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-11T04:15:00+03:00"
            task["completed_at"] = "2026-08-11T04:45:00+03:00"
        if task["task_id"] == "TASK-0807":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-11T04:50:00+03:00"
            task["completed_at"] = "2026-08-11T05:20:00+03:00"
        if task["task_id"] == "TASK-0808":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-11T05:25:00+03:00"
            task["completed_at"] = "2026-08-11T05:30:00+03:00"
        if task["task_id"] == "TASK-0709":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-11T22:00:00+03:00"
            task["completed_at"] = "2026-08-11T19:05:00+03:00"
        if task["task_id"] == "TASK-0710":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-11T19:10:00+03:00"
            task["completed_at"] = "2026-08-11T19:40:00+03:00"
        if task["task_id"] == "TASK-0809":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-11T21:45:00+03:00"
            task["completed_at"] = "2026-08-12T00:25:00+03:00"
        if task["task_id"] == "TASK-0810":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-12T00:30:00+03:00"
            task["completed_at"] = "2026-08-12T02:15:00+03:00"
        if task["task_id"] == "TASK-2201":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-12T08:50:00+03:00"
            task["completed_at"] = "2026-08-12T09:20:00+03:00"
        if task["task_id"] == "TASK-2202":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-12T09:25:00+03:00"
            task["completed_at"] = "2026-08-12T10:40:00+03:00"
        if task["task_id"] == "TASK-2203":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-12T10:45:00+03:00"
            task["completed_at"] = "2026-08-12T11:15:00+03:00"
        if task["task_id"] == "TASK-2204":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-12T11:20:00+03:00"
            task["completed_at"] = "2026-08-12T13:30:00+03:00"
        if task["task_id"] == "TASK-2205":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-12T13:35:00+03:00"
            task["completed_at"] = "2026-08-12T14:40:00+03:00"
        if task["task_id"] == "TASK-2206":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-12T14:45:00+03:00"
            task["completed_at"] = "2026-08-12T15:20:00+03:00"
        if task["task_id"] == "TASK-2207":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-12T15:25:00+03:00"
            task["completed_at"] = "2026-08-12T16:10:00+03:00"
        if task["task_id"] == "TASK-2208":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-12T16:15:00+03:00"
            task["completed_at"] = "2026-08-12T18:00:00+03:00"
        if task["task_id"] == "TASK-2209":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-12T22:59:00+03:00"
            task["completed_at"] = "2026-08-13T00:08:00+03:00"
        if task["task_id"] == "TASK-2211":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-13T00:10:00+03:00"
            task["completed_at"] = "2026-08-13T00:35:00+03:00"
        if task["task_id"] == "TASK-2301":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-13T09:00:00+03:00"
            task["completed_at"] = "2026-08-13T09:45:00+03:00"
        if task["task_id"] == "TASK-2401":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-13T14:00:00+03:00"
            task["completed_at"] = "2026-08-13T17:00:00+03:00"
        if task["task_id"] == "TASK-2402":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-13T17:05:00+03:00"
            task["completed_at"] = "2026-08-13T17:35:00+03:00"
        if task["task_id"] == "TASK-2403":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-13T17:36:00+03:00"
            task["completed_at"] = "2026-08-13T17:45:00+03:00"
        if task["task_id"] == "TASK-2501":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-13T21:50:00+03:00"
            task["completed_at"] = "2026-08-13T22:45:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-2601":
            task["attempts"] = 1
            task["started_at"] = "2026-08-13T22:50:00+03:00"
            task["last_error"] = None
            task["completed_at"] = "2026-08-14T14:45:00+03:00"
        if task["task_id"] == "TASK-2701":
            task["attempts"] = 1
            task["started_at"] = "2026-08-14T15:00:00+03:00"
            task["last_error"] = None
            task["completed_at"] = "2026-08-14T17:00:00+03:00"
        if task["task_id"] == "TASK-2702":
            task["attempts"] = 1
            task["started_at"] = "2026-08-14T17:20:00+03:00"
            task["last_error"] = None
            task["completed_at"] = "2026-08-14T18:05:00+03:00"
        if task["task_id"] == "TASK-2703":
            task["attempts"] = 1
            task["started_at"] = "2026-08-14T18:06:00+03:00"
            task["last_error"] = None
            task["completed_at"] = "2026-08-14T18:35:00+03:00"
        if task["task_id"] == "TASK-2704":
            task["attempts"] = 1
            task["started_at"] = "2026-08-14T18:36:00+03:00"
            task["last_error"] = None
            task["completed_at"] = "2026-08-14T19:10:00+03:00"
        if task["task_id"] == "TASK-2717":
            task["status"] = "DONE"
            task["attempts"] = 1
            task["started_at"] = "2026-08-14T19:11:00+03:00"
            task["completed_at"] = "2026-08-14T19:57:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-2801":
            task["attempts"] = 2
            task["started_at"] = "2026-08-16T19:30:00+03:00"
            task["completed_at"] = "2026-08-16T20:55:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-2802":
            task["attempts"] = 2
            task["started_at"] = "2026-08-16T21:00:00+03:00"
            task["completed_at"] = "2026-08-16T22:45:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-2803":
            task["attempts"] = 1
            task["started_at"] = "2026-08-16T23:00:00+03:00"
            task["completed_at"] = "2026-08-17T01:10:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-2804":
            task["attempts"] = 1
            task["started_at"] = "2026-08-17T11:00:00+03:00"
            task["completed_at"] = "2026-08-17T14:45:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-2805":
            task["attempts"] = 1
            task["started_at"] = "2026-08-17T15:00:00+03:00"
            task["completed_at"] = "2026-08-17T18:00:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-2806":
            task["attempts"] = 2
            task["started_at"] = "2026-08-17T19:00:00+03:00"
            task["completed_at"] = "2026-08-17T21:50:00+03:00"
            task["last_error"] = None
        if task["task_id"] in {"TASK-2901", "TASK-2902", "TASK-2903", "TASK-2904", "TASK-2905",
                                "TASK-2906", "TASK-2907", "TASK-2908", "TASK-2909", "TASK-2910"}:
            task["attempts"] = 1
            task["started_at"] = "2026-08-18T09:00:00+03:00"
            task["completed_at"] = "2026-08-18T13:30:00+03:00"
            task["last_error"] = None
        if task["task_id"] in {"TASK-3001", "TASK-3002", "TASK-3003", "TASK-3004", "TASK-3005",
                                "TASK-3006", "TASK-3007", "TASK-3008", "TASK-3009", "TASK-3010",
                                "TASK-3011", "TASK-3012"}:
            task["attempts"] = 1
            task["started_at"] = "2026-08-23T14:00:00+03:00"
            task["completed_at"] = "2026-08-24T02:00:00+03:00"
            task["last_error"] = None
        if task["task_id"] in {"TASK-3013", "TASK-3014", "TASK-3015", "TASK-3016", "TASK-3017",
                                "TASK-3018", "TASK-3019", "TASK-3020", "TASK-3021", "TASK-3022"}:
            task["attempts"] = 1
            task["started_at"] = "2026-08-24T14:00:00+03:00"
            task["completed_at"] = "2026-08-24T22:15:00+03:00"
            task["last_error"] = None
        if task["task_id"] in {"TASK-3023", "TASK-3024", "TASK-3025", "TASK-3026", "TASK-3027",
                                "TASK-3028", "TASK-3029", "TASK-3030", "TASK-3031", "TASK-3032",
                                "TASK-3033"}:
            task["attempts"] = 1
            task["started_at"] = "2026-08-25T13:00:00+03:00"
            task["completed_at"] = "2026-08-25T15:30:00+03:00"
            task["last_error"] = None
        if task["task_id"] in {"TASK-3101", "TASK-3102", "TASK-3103", "TASK-3104", "TASK-3105"}:
            task["attempts"] = 1
            task["started_at"] = "2026-08-25T22:00:00+03:00"
            task["completed_at"] = "2026-08-25T23:30:00+03:00"
            task["last_error"] = None
        if task["task_id"] in {"TASK-3301", "TASK-3302", "TASK-3303", "TASK-3304", "TASK-3305",
                                "TASK-3306", "TASK-3307", "TASK-3308"}:
            task["attempts"] = 1
            task["started_at"] = "2026-08-26T14:00:00+03:00"
            task["completed_at"] = "2026-08-26T15:35:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3309":
            task["attempts"] = 1
            task["started_at"] = "2026-08-26T19:30:00+03:00"
            task["completed_at"] = "2026-08-26T22:15:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3310":
            task["attempts"] = 1
            task["started_at"] = "2026-08-26T22:30:00+03:00"
            task["completed_at"] = "2026-08-26T23:45:00+03:00"
            task["last_error"] = None
        if task["task_id"] in {"TASK-3401", "TASK-3402", "TASK-3403", "TASK-3404"}:
            task["attempts"] = 1
            task["started_at"] = "2026-08-27T00:00:00+03:00"
            task["completed_at"] = "2026-08-27T02:30:00+03:00"
            task["last_error"] = None
        if task["task_id"] in {"TASK-3405", "TASK-3406", "TASK-3407"}:
            task["attempts"] = 1
            task["started_at"] = "2026-08-28T11:00:00+03:00"
            task["completed_at"] = "2026-08-28T12:00:00+03:00"
            task["last_error"] = None
        if task["task_id"] in {"TASK-3501", "TASK-3502", "TASK-3503", "TASK-3504", "TASK-3505", "TASK-3506"}:
            task["attempts"] = 1
            task["started_at"] = "2026-08-29T22:00:00+03:00"
            task["completed_at"] = "2026-08-29T23:30:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3507":
            task["attempts"] = 1
            task["started_at"] = "2026-08-29T23:30:00+03:00"
            task["completed_at"] = "2026-08-30T00:00:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3508":
            task["attempts"] = 1
            task["started_at"] = "2026-08-31T09:00:00+03:00"
            task["completed_at"] = "2026-08-31T11:30:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3601":
            task["attempts"] = 1
            task["started_at"] = "2026-08-31T12:00:00+03:00"
            task["completed_at"] = "2026-08-31T21:30:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3701":
            task["attempts"] = 1
            task["started_at"] = "2026-08-31T21:35:00+03:00"
            task["completed_at"] = "2026-08-31T23:55:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3702":
            task["attempts"] = 1
            task["started_at"] = "2026-08-31T23:56:00+03:00"
            task["completed_at"] = "2026-09-01T15:35:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3703":
            task["attempts"] = 1
            task["started_at"] = "2026-09-01T15:40:00+03:00"
            task["completed_at"] = "2026-09-01T16:10:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3704":
            task["attempts"] = 1
            task["started_at"] = "2026-09-07T21:20:00+03:00"
            task["completed_at"] = "2026-09-07T21:40:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3705":
            task["attempts"] = 1
            task["started_at"] = "2026-09-09T17:20:00+03:00"
            task["completed_at"] = "2026-09-09T17:55:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3711":
            task["attempts"] = 1
            task["started_at"] = "2026-09-14T20:30:00+03:00"
            task["completed_at"] = "2026-09-14T21:20:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3712":
            task["attempts"] = 1
            task["started_at"] = "2026-09-14T21:30:00+03:00"
            task["completed_at"] = "2026-09-14T22:15:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3713":
            task["attempts"] = 1
            task["started_at"] = "2026-09-15T09:00:00+03:00"
            task["completed_at"] = "2026-09-15T10:30:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3715":
            task["attempts"] = 1
            task["started_at"] = "2026-09-15T22:00:00+03:00"
            task["completed_at"] = "2026-09-15T23:00:00+03:00"
            task["last_error"] = "BLOCKED: no authenticated Vercel deployment access in this environment (vercel whoami -> Logged out; no token; no project link; no MCP deployment tool)."
        if task["task_id"] == "TASK-3716":
            task["attempts"] = 1
            task["started_at"] = "2026-09-17T16:30:00+03:00"
            task["completed_at"] = "2026-09-17T17:00:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3714":
            task["attempts"] = 1
            task["started_at"] = "2026-09-17T22:20:00+03:00"
            task["completed_at"] = "2026-09-17T22:45:00+03:00"
            task["last_error"] = "BLOCKED: no real coaches/sessions available for the pilot; PILOT STATUS = NOT_STARTED. No participants, sessions, observations, or findings were fabricated."
        if task["task_id"] == "TASK-3718":
            task["attempts"] = 1
            task["started_at"] = "2026-09-21T15:30:00+03:00"
            task["completed_at"] = "2026-09-21T17:15:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3719":
            task["attempts"] = 1
            task["started_at"] = "2026-09-21T21:30:00+03:00"
            task["completed_at"] = "2026-09-21T22:15:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3720":
            task["attempts"] = 1
            task["started_at"] = "2026-09-23T16:30:00+03:00"
            task["completed_at"] = "2026-09-23T18:00:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-3721":
            task["attempts"] = 1
            task["started_at"] = "2026-09-23T18:15:00+03:00"
            task["completed_at"] = "2026-09-23T21:00:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-2705":
            task["attempts"] = 1
            task["started_at"] = "2026-08-14T20:05:00+03:00"
            task["last_error"] = None
            task["completed_at"] = "2026-08-14T20:20:00+03:00"
        if task["task_id"] == "TASK-2706":
            task["attempts"] = 2
            task["started_at"] = "2026-08-14T20:21:00+03:00"
            task["last_error"] = None
            task["completed_at"] = "2026-08-15T15:40:00+03:00"
        if task["task_id"] == "TASK-2707":
            task["attempts"] = 1
            task["started_at"] = "2026-08-14T20:36:00+03:00"
            task["last_error"] = None
            task["completed_at"] = "2026-08-14T20:55:00+03:00"
        if task["task_id"] == "TASK-2711":
            task["attempts"] = 1
            task["started_at"] = "2026-08-14T20:56:00+03:00"
            task["last_error"] = None
            task["completed_at"] = "2026-08-14T21:12:00+03:00"
        if task["task_id"] == "TASK-2710":
            task["attempts"] = 1
            task["started_at"] = "2026-08-14T21:13:00+03:00"
            task["last_error"] = None
            task["completed_at"] = "2026-08-15T06:35:00+03:00"
        if task["task_id"] == "TASK-2708":
            task["attempts"] = 1
            task["started_at"] = "2026-08-15T22:45:00+03:00"
            task["completed_at"] = "2026-08-15T23:02:00+03:00"
            task["last_error"] = None
        if task["task_id"] == "TASK-2709":
            task["attempts"] = 1
            task["started_at"] = "2026-08-15T23:03:00+03:00"
            task["last_error"] = None
            task["completed_at"] = "2026-08-15T23:09:00+03:00"
        if task["task_id"] == "TASK-2712":
            task["attempts"] = 1
            task["started_at"] = "2026-08-15T23:09:00+03:00"
            task["last_error"] = None
            task["completed_at"] = "2026-08-15T23:13:00+03:00"
    return {
        "schema_version": "2.0.0",
        "generated_at": "2026-07-30",
        "generator": "scripts/generate_task_registry.py",
        "progress_method": "Suma weight_percent pentru taskurile DONE; taskurile parțiale nu contribuie.",
        "tasks": TASKS,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    generated = json.dumps(materialize(), ensure_ascii=False, indent=2) + "\n"
    if args.check:
        if not REGISTRY.exists() or REGISTRY.read_text(encoding="utf-8") != generated:
            print("TASK_REGISTRY.json nu corespunde generatorului.")
            return 1
        print(f"Registrul este reproductibil: {len(TASKS)} taskuri.")
        return 0
    REGISTRY.write_text(generated, encoding="utf-8")
    print(f"Generat {REGISTRY}: {len(TASKS)} taskuri.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
