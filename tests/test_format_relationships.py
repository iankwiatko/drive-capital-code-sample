import unittest

from src.format_relationships import format_relationships
from src.models import Relationship


class FormatRelationshipsTests(unittest.TestCase):
    def test_no_relationships_gives_empty_string(self):
        self.assertEqual(format_relationships([]), "")

    def test_one_line_per_company_in_order(self):
        relationships = [
            Relationship("ACME", None, 0),
            Relationship("Globex", "Chris", 2),
        ]
        self.assertEqual(
            format_relationships(relationships),
            "ACME: No current relationship\nGlobex: Chris (2)",
        )


if __name__ == "__main__":
    unittest.main()
