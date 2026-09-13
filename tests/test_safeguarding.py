from __future__ import annotations

import copy
import json
import unittest
from datetime import date

from jsonschema import Draft202012Validator

from scripts.validate_safeguarding import ROOT, validate, validate_payload


class SafeguardingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "data/safeguarding/canonical.json").read_text(encoding="utf-8"))
        cls.schema = json.loads((ROOT / "schemas/safeguarding.schema.json").read_text(encoding="utf-8"))

    def mutated(self):
        return copy.deepcopy(self.data)

    def test_01_canonical_schema(self):
        self.assertFalse(list(Draft202012Validator(self.schema).iter_errors(self.data)))

    def test_02_canonical_validator(self):
        self.assertEqual(validate(today=date(2026, 7, 30)), [])

    def test_03_legal_basis_missing(self):
        data = self.mutated(); data["requirements"][0]["exact_article_or_section"] = None
        self.assertTrue(any(x.startswith("LEGAL_BASIS_MISSING") for x in validate_payload(data)))

    def test_04_legal_scope_unclear(self):
        data = self.mutated()
        item = next(x for x in data["requirements"] if x["status"] == "FRF_REQUIREMENT")
        item["applies_to"] = []
        self.assertTrue(any(x.startswith("LEGAL_SCOPE_UNCLEAR") for x in validate_payload(data)))

    def test_05_review_required_is_explained(self):
        flagged = [x for x in self.data["requirements"] if x["legal_review_required"]]
        self.assertTrue(flagged and all(x["uncertainty"] for x in flagged))

    def test_06_safeguarding_role_exists(self):
        self.assertTrue(any(x["role"] == "responsabil safeguarding" for x in self.data["roles"]))

    def test_07_reporting_chain_complete(self):
        self.assertTrue(all(x["reports_to"] for x in self.data["roles"]))

    def test_08_risk_controls_complete(self):
        self.assertTrue(all(x["preventive_control"] for x in self.data["risks"]))

    def test_09_contacts_verified(self):
        self.assertTrue(all(x["verified_at"] and x["source_url"] for x in self.data["contacts"]))

    def test_10_contacts_not_overdue_at_reference_date(self):
        self.assertFalse(any(x.startswith("CONTACT_RECHECK_OVERDUE")
                             for x in validate_payload(self.data, today=date(2026, 7, 30))))

    def test_11_overdue_contact_detected(self):
        data = self.mutated(); data["contacts"][0]["recheck_at"] = "2026-01-01"
        self.assertTrue(any(x.startswith("CONTACT_RECHECK_OVERDUE")
                            for x in validate_payload(data, today=date(2026, 7, 30))))

    def test_12_exactly_30_situations(self):
        self.assertEqual(len(self.data["situations"]), 30)

    def test_13_exactly_10_disclosure_scripts(self):
        self.assertEqual(len(self.data["scripts"]), 10)

    def test_14_at_least_20_instruments(self):
        self.assertGreaterEqual(len(self.data["instruments"]), 20)

    def test_15_no_absolute_confidentiality(self):
        self.assertFalse(any(x.startswith("ABSOLUTE_CONFIDENTIALITY_PROMISED")
                             for x in validate_payload(self.data)))

    def test_16_absolute_confidentiality_detected(self):
        data = self.mutated(); data["scripts"][0]["coach_says"] = "Nu spun nimănui."
        self.assertTrue(any(x.startswith("ABSOLUTE_CONFIDENTIALITY_PROMISED")
                            for x in validate_payload(data)))

    def test_17_no_unauthorized_investigation(self):
        self.assertFalse(any(x.startswith("UNAUTHORIZED_INVESTIGATION_INSTRUCTION")
                             for x in validate_payload(self.data)))

    def test_18_unauthorized_investigation_detected(self):
        data = self.mutated(); data["scripts"][0]["coach_action"] = "Confruntă presupusul autor."
        self.assertTrue(any(x.startswith("UNAUTHORIZED_INVESTIGATION_INSTRUCTION")
                            for x in validate_payload(data)))

    def test_19_no_child_blaming(self):
        self.assertFalse(any(x.startswith("CHILD_BLAMING_LANGUAGE") for x in validate_payload(self.data)))

    def test_20_child_blaming_detected(self):
        data = self.mutated(); data["scripts"][0]["coach_action"] = "E vina ta."
        self.assertTrue(any(x.startswith("CHILD_BLAMING_LANGUAGE") for x in validate_payload(data)))

    def test_21_real_cnp_detected(self):
        data = self.mutated(); data["scripts"][0]["coach_action"] = "CNP 1960523420018"
        self.assertTrue(any(x.startswith("REAL_PERSONAL_DATA_DETECTED") for x in validate_payload(data)))

    def test_22_public_contact_numbers_allowed(self):
        self.assertFalse(any(x.startswith("REAL_PERSONAL_DATA_DETECTED") for x in validate_payload(self.data)))

    def test_23_safe_recruitment_instrument(self):
        self.assertTrue(any("recrut" in x.lower() for x in self.data["instruments"]))

    def test_24_visual_consent_instrument(self):
        self.assertTrue(any("vizual" in x.lower() or "imagine" in x.lower() or "fotograf" in x.lower()
                            for x in self.data["instruments"]))

    def test_25_travel_risk_instrument(self):
        self.assertTrue(any("deplas" in x.lower() for x in self.data["instruments"]))

    def test_26_professional_boundary_instrument(self):
        self.assertTrue(any("conduit" in x.lower() or "limite" in x.lower()
                            for x in self.data["instruments"]))

    def test_27_single_pedagogical_group(self):
        text = (ROOT / "research/dossiers/safeguarding.md").read_text(encoding="utf-8")
        self.assertIn("2015 și 2016", text)

    def test_28_status_vocabulary_is_explicit(self):
        statuses = {x["status"] for x in self.data["requirements"]}
        self.assertTrue({"LEGAL_REQUIREMENT_ROMANIA", "FRF_REQUIREMENT",
                         "FIFA_STANDARD", "UEFA_STANDARD"} <= statuses)

    def test_29_svg_accessibility(self):
        for name in ("disclosure-response.svg", "escalation.svg", "trusted-adults.svg"):
            text = (ROOT / "assets/safeguarding" / name).read_text(encoding="utf-8")
            self.assertIn("<title", text); self.assertIn("<desc", text)

    def test_30_deterministic_result(self):
        self.assertEqual(validate(today=date(2026, 7, 30)), validate(today=date(2026, 7, 30)))


if __name__ == "__main__":
    unittest.main()
