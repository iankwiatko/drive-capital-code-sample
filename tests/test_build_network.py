import unittest

from src.build_network import NetworkCreationError, build_network
from src.models import Company, Contact, Employee, Network, Partner


class BuildNetworkTests(unittest.TestCase):
    def test_empty_command_list_returns_empty_network(self):
        self.assertEqual(build_network([]), Network())

    def test_populates_network_from_commands(self):
        network = build_network(
            [
                Partner("Chris"),
                Company("Globex"),
                Employee("Laurie", "Globex"),
                Contact("Laurie", "Chris", "email"),
                Contact("Laurie", "Chris", "coffee"),
            ]
        )
        self.assertEqual(network.partners, {Partner("Chris")})
        self.assertEqual(network.companies, {Company("Globex")})
        self.assertEqual(network.employees, {"Laurie": Employee("Laurie", "Globex")})
        self.assertEqual(
            network.contacts,
            [Contact("Laurie", "Chris", "email"), Contact("Laurie", "Chris", "coffee")],
        )

    def test_duplicate_partner_and_company_are_ignored(self):
        network = build_network(
            [Partner("Chris"), Partner("Chris"), Company("Globex"), Company("Globex")]
        )
        self.assertEqual(network.partners, {Partner("Chris")})
        self.assertEqual(network.companies, {Company("Globex")})

    def test_invalid_commands_raise(self):
        cases = {
            "unknown company": [Employee("Laurie", "Globex")],
            "unknown partner": [
                Company("Globex"),
                Employee("Laurie", "Globex"),
                Contact("Laurie", "Nobody", "email"),
            ],
            "unknown employee": [Partner("Chris"), Contact("Nobody", "Chris", "email")],
            "duplicate employee": [
                Company("Globex"),
                Company("Hooli"),
                Employee("Laurie", "Globex"),
                Employee("Laurie", "Hooli"),
            ],
            "declared out of order": [
                Company("Globex"),
                Contact("Laurie", "Chris", "email"),
                Partner("Chris"),
                Employee("Laurie", "Globex"),
            ],
        }
        for name, commands in cases.items():
            with self.subTest(case=name):
                with self.assertRaises(NetworkCreationError):
                    build_network(commands)

    def test_unrecognized_command_raises(self):
        with self.assertRaises(NetworkCreationError):
            build_network([object()])


if __name__ == "__main__":
    unittest.main()
