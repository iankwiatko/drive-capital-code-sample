import unittest

from src.build_network import build_network
from src.command_parser import parse_commands
from src.models import Network, Relationship
from src.strongest_partners import strongest_partners


def strongest_from(content):
    return strongest_partners(build_network(parse_commands(content)))


class StrongestPartnersTests(unittest.TestCase):
    def test_empty_network_returns_no_relationships(self):
        self.assertEqual(strongest_partners(Network()), [])

    def test_company_without_contacts_has_no_partner(self):
        self.assertEqual(
            strongest_from("Company Globex"), [Relationship("Globex", None, 0)]
        )

    def test_partner_with_most_contacts_wins(self):
        content = (
            "Partner Chris\nPartner Molly\nCompany Globex\nEmployee Laurie Globex\n"
            "Contact Laurie Molly call\nContact Laurie Chris email\n"
            "Contact Laurie Chris coffee\n"
        )
        self.assertEqual(strongest_from(content), [Relationship("Globex", "Chris", 2)])

    def test_ties_are_broken_alphabetically(self):
        content = (
            "Partner Molly\nPartner Chris\nCompany Globex\nEmployee Laurie Globex\n"
            "Contact Laurie Molly call\nContact Laurie Chris email\n"
        )
        self.assertEqual(strongest_from(content), [Relationship("Globex", "Chris", 1)])

    def test_contacts_from_all_employees_of_a_company_are_combined(self):
        content = (
            "Partner Chris\nPartner Molly\nCompany Globex\n"
            "Employee Laurie Globex\nEmployee Jamie Globex\n"
            "Contact Laurie Molly call\nContact Laurie Chris email\n"
            "Contact Jamie Molly email\n"
        )
        self.assertEqual(strongest_from(content), [Relationship("Globex", "Molly", 2)])

    def test_results_are_scored_per_company_and_ordered_by_name(self):
        content = (
            "Partner Chris\nPartner Molly\nCompany Hooli\nCompany Globex\n"
            "Employee Laurie Globex\nEmployee Abdi Hooli\n"
            "Contact Laurie Chris email\nContact Abdi Molly email\n"
        )
        self.assertEqual(
            strongest_from(content),
            [Relationship("Globex", "Chris", 1), Relationship("Hooli", "Molly", 1)],
        )

    def test_sample_input(self):
        content = (
            "Partner Chris\nPartner Molly\nCompany Globex\nCompany ACME\n"
            "Employee Laurie Globex\nCompany Hooli\nEmployee Abdi Hooli\n"
            "Employee Jamie Globex\nContact Laurie Chris email\n"
            "Contact Laurie Molly call\nPartner Rezzan\n"
            "Contact Abdi Molly email\nContact Laurie Chris coffee\n"
        )
        self.assertEqual(
            strongest_from(content),
            [
                Relationship("ACME", None, 0),
                Relationship("Globex", "Chris", 2),
                Relationship("Hooli", "Molly", 1),
            ],
        )


if __name__ == "__main__":
    unittest.main()
