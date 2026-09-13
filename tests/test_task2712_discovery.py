import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class DiscoveryTests(unittest.TestCase):
 def test_static_index_and_explanations(self):
  text=(ROOT/'app/src/lib/discovery-index.ts').read_text(encoding='utf-8')
  for kind in ('PROBLEMĂ','PRINCIPIU','EXERCIȚIU','ȘEDINȚĂ','EVALUARE','CAPITOL'): self.assertIn(kind,text)
  self.assertIn('scoreDiscovery',text);self.assertIn('explainDiscovery',text)
  self.assertIn('playersMin:8,playersMax:18',text)
 def test_no_semantic_backend(self):
  text=(ROOT/'app/src/lib/discovery-index.ts').read_text(encoding='utf-8').lower()
  for forbidden in ('openai','vector db','elasticsearch'): self.assertNotIn(forbidden,text)
 def test_page_has_accessible_filters_and_empty_state(self):
  text=(ROOT/'app/src/pages/cauta.astro').read_text(encoding='utf-8')
  self.assertIn('aria-live="polite"',text);self.assertIn('Nu am găsit',text);self.assertIn('id="reset"',text)
if __name__=='__main__':unittest.main()
