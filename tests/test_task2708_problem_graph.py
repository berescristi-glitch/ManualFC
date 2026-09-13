import json
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]

class Wave3ProblemGraphTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.library = json.loads((ROOT/'data/problems/problem-library.json').read_text(encoding='utf-8'))
        cls.problems = cls.library['problems']

    def test_schema_and_flagship_count(self):
        schema = json.loads((ROOT/'schemas/problem.schema.json').read_text(encoding='utf-8'))
        self.assertFalse(list(Draft202012Validator(schema).iter_errors(self.library)))
        self.assertGreaterEqual(len(self.problems), 8)
        self.assertEqual(sum(bool(p['flagship']) for p in self.problems), 3)

    def test_stable_ids_and_observation_cause_separation(self):
        ids=[]
        for p in self.problems:
            ids.append(p['problem_id'])
            self.assertNotEqual(p['what_is_seen'], p['what_is_not_known'])
            self.assertTrue(all(x['evidence_state'] in ('HYPOTHESIS','NEEDS_RESEARCH','PRACTICE_HEURISTIC') for x in p['possible_explanations']))
            self.assertTrue(p['quick_tests'][0]['interpretation_limit'])
        self.assertEqual(len(ids), len(set(ids)))

    def test_graph_targets_exist(self):
        principles={json.loads(p.read_text(encoding='utf-8'))['id'] for p in (ROOT/'data/principles').glob('*.json')}
        exercises={json.loads(p.read_text(encoding='utf-8'))['id'] for p in (ROOT/'data/exercises').glob('*.json')}
        sessions={json.loads(p.read_text(encoding='utf-8'))['id'] for p in (ROOT/'data/sessions').glob('*.json')}
        assessments={json.loads(p.read_text(encoding='utf-8'))['id'] for p in (ROOT/'data/assessments').glob('*.json')}
        claims={c['claim_id'] for c in json.loads((ROOT/'research/claims.json').read_text(encoding='utf-8'))['claims']}
        for p in self.problems:
            self.assertTrue(set(p['related_principles']) <= principles)
            self.assertTrue(set(p['related_exercises']) <= exercises)
            self.assertTrue(set(p['related_sessions']) <= sessions)
            self.assertTrue(set(p['assessment_links']) <= assessments)
            self.assertTrue(set(p['evidence_claim_ids']) <= claims)

    def test_no_diagnostic_language(self):
        forbidden=('adhd','anxietate are','lipsă de inteligență','leneș','diagnostic')
        for p in self.problems:
            public=' '.join([p['human_title'],p['observable_behavior'],p['what_is_seen']]).lower()
            for term in forbidden: self.assertNotIn(term, public)

if __name__ == '__main__': unittest.main()
