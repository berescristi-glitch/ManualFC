import tempfile
import unittest
from pathlib import Path

from scripts.validate_html_landmarks import validate


class HtmlLandmarkTests(unittest.TestCase):
    def test_accepts_exactly_one_main(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            (path / "index.html").write_text("<html><body><main><article></article></main></body></html>", encoding="utf-8")
            self.assertEqual(validate(path), [])

    def test_rejects_nested_and_multiple_main(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            (path / "index.html").write_text("<main><main></main></main>", encoding="utf-8")
            errors = validate(path)
            self.assertTrue(any("main_count=2" in error for error in errors))
            self.assertTrue(any("nested_main=1" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
