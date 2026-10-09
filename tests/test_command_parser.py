import unittest

from src.command_parser import parse_commands
from src.models import Company, Contact, Employee, Partner


class CommandParserTests(unittest.TestCase):
    def test_empty_input_returns_no_commands(self):
        self.assertEqual(parse_commands(""), [])

    def test_parses_each_command_in_order(self):
        content = (
            "Partner Chris\nCompany Globex\n"
            "Employee Laurie Globex\nContact Laurie Chris email\n"
        )
        self.assertEqual(
            parse_commands(content),
            [
                Partner("Chris"),
                Company("Globex"),
                Employee("Laurie", "Globex"),
                Contact("Laurie", "Chris", "email"),
            ],
        )

    def test_accepts_every_contact_kind(self):
        for kind in ("coffee", "call", "email"):
            with self.subTest(kind=kind):
                self.assertEqual(
                    parse_commands(f"Contact Laurie Chris {kind}"),
                    [Contact("Laurie", "Chris", kind)],
                )

    def test_invalid_lines_raise(self):
        for line in (
            "Vendor Acme",
            "Partner",
            "Employee Laurie",
            "Partner Chris Molly",
            "Contact Laurie Chris email extra",
            "Contact Laurie Chris invalid",
        ):
            with self.subTest(line=line), self.assertRaises(ValueError):
                parse_commands(line)

    def test_error_message_includes_the_invalid_line(self):
        with self.assertRaisesRegex(ValueError, "Vendor Acme"):
            parse_commands("Partner Chris\nVendor Acme")


if __name__ == "__main__":
    unittest.main()
