import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SESSION_DIR = ROOT / "data" / "sessions"


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_session(filename):
    return json.loads((SESSION_DIR / filename).read_text(encoding="utf-8"))


class Task2205SessionSystemTests(unittest.TestCase):
    SESSION_FILES = ["session-introducere.json", "session-coordonare-si-transfer.json"]

    def test_session_files_exist(self):
        for filename in self.SESSION_FILES:
            self.assertTrue((SESSION_DIR / filename).exists(), filename)

    def test_ids_unique(self):
        ids = [load_session(f)["id"] for f in self.SESSION_FILES]
        self.assertEqual(ids, ["SES-0001", "SES-0002"])

    def test_duration_matches_schema_enum(self):
        for filename in self.SESSION_FILES:
            ses = load_session(filename)
            self.assertIn(ses["duration_min"], (60, 75, 90))

    def test_segments_are_contiguous_and_cover_full_duration(self):
        for filename in self.SESSION_FILES:
            ses = load_session(filename)
            segments = sorted(ses["segments"], key=lambda s: s["start_min"])
            self.assertEqual(segments[0]["start_min"], 0)
            self.assertEqual(segments[-1]["end_min"], ses["duration_min"])
            for a, b in zip(segments, segments[1:]):
                self.assertEqual(a["end_min"], b["start_min"], f"{filename}: gap/overlap between segments")

    def test_at_least_three_segments(self):
        for filename in self.SESSION_FILES:
            ses = load_session(filename)
            self.assertGreaterEqual(len(ses["segments"]), 3)

    def test_every_segment_answers_why_now(self):
        for filename in self.SESSION_FILES:
            ses = load_session(filename)
            for seg in ses["segments"]:
                self.assertTrue(seg["why_now"].strip(), f"{filename}: {seg['title']}")

    def test_exercise_ids_referenced_exist_and_match_progression_order(self):
        exercise_dir = ROOT / "data" / "exercises"
        known_ids = set()
        for f in exercise_dir.glob("exercise-*.json"):
            known_ids.add(json.loads(f.read_text(encoding="utf-8"))["id"])
        ses1 = load_session("session-introducere.json")
        ses1_exercise_ids = [eid for seg in ses1["segments"] for eid in seg["exercise_ids"]]
        self.assertEqual(ses1_exercise_ids, ["EX-0001", "EX-0002", "EX-0003"])
        for eid in ses1_exercise_ids:
            self.assertIn(eid, known_ids)
        ses2 = load_session("session-coordonare-si-transfer.json")
        ses2_exercise_ids = [eid for seg in ses2["segments"] for eid in seg["exercise_ids"]]
        self.assertEqual(ses2_exercise_ids, ["EX-0004", "EX-0005"])

    def test_second_session_count_justified_not_assumed(self):
        ses2 = load_session("session-coordonare-si-transfer.json")
        self.assertIn("alegere practică ManualFC", ses2["session_rationale"])
        self.assertNotIn("regulă validată", ses2["session_rationale"])

    def test_no_command_shouting_during_transfer_game(self):
        ses2 = load_session("session-coordonare-si-transfer.json")
        transfer_segment = next(s for s in ses2["segments"] if "EX-0005" in s["exercise_ids"])
        self.assertIn("fără comenzi verbale", transfer_segment["intervention_criteria"][0])

    def test_reflection_present_and_no_fabricated_duration(self):
        for filename in self.SESSION_FILES:
            ses = load_session(filename)
            self.assertGreaterEqual(len(ses["reflection"]), 1)
            text = json.dumps(ses, ensure_ascii=False)
            self.assertNotIn("3-5 minute", text)
            self.assertNotIn("3–5 minute", text)

    def test_no_withdrawn_source_referenced(self):
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        for filename in self.SESSION_FILES:
            ses = load_session(filename)
            for sid in ses["sources"]:
                self.assertIn(sid, sources, f"{filename} references unknown {sid}")
                self.assertFalse(sources[sid]["withdrawn"], f"{filename} references withdrawn {sid}")

    def test_safety_routine_reused_not_reinvented(self):
        # PHASE-25: raw internal claim/chapter codes (CLM-xxxx, CH-0405)
        # rendered verbatim in product UI are a defect, closed in PHASE-25 —
        # both are now named in plain language instead of by internal code.
        ses1 = load_session("session-introducere.json")
        warmup = ses1["segments"][0]
        self.assertNotIn("CH-0405", warmup["why_now"])
        self.assertIn("organizare și siguranță", warmup["why_now"])
        self.assertNotIn("CLM-0097", warmup["why_now"])
        self.assertIn("FIFA 11+ Kids", warmup["why_now"])


if __name__ == "__main__":
    unittest.main()
