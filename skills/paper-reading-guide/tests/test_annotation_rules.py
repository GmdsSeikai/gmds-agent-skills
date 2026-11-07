"""Pin source/claim boundaries; this does not prove model compliance."""
from pathlib import Path
import unittest


RULES = Path(__file__).resolve().parents[1] / "references" / "evidence-rules.md"


class AnnotationRuleTests(unittest.TestCase):
    def test_annotation_cannot_be_claimed_as_author_content(self):
        rules = RULES.read_text(encoding="utf-8")
        self.assertIn("Never present teaching annotations as author content.", rules)
        self.assertIn("A callout leader locates a feature; it does not establish a causal claim.", rules)


if __name__ == "__main__":
    unittest.main()
