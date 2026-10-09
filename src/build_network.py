"""Builds a network from a list of commands by processing each command sequentially, and assigning entities to the appropriate collections within the network. Raises NetworkCreationError if any inconsistencies or unknown references are encountered."""

from .models import Command, Company, Contact, Employee, Network, Partner


class NetworkCreationError(Exception):
    """Raised when there is an error creating the network."""


def build_network(commands: list[Command]) -> Network:
    network = Network()

    for command in commands:
        match command:
            case Partner():
                network.partners.add(command)
            case Company():
                network.companies.add(command)
            case Employee(name=name, company=company):
                # ensuring that employee names are unique within the network
                if name in network.employees:
                    raise NetworkCreationError(f"duplicate employee: {name!r}")
                # raise an error if the employee company has not been declared
                if Company(company) not in network.companies:
                    raise NetworkCreationError(
                        f"employee refers to unknown company: {company!r}"
                    )
                network.employees[name] = command
            case Contact(employee=employee, partner=partner):
                # raise error if the contact references unknown employee
                if employee not in network.employees:
                    raise NetworkCreationError(
                        f"contact refers to unknown employee: {employee!r}"
                    )
                # raise error if the contact references unknown partner
                if Partner(partner) not in network.partners:
                    raise NetworkCreationError(
                        f"contact refers to unknown partner: {partner!r}"
                    )
                network.contacts.append(command)
            case _:
                raise NetworkCreationError(f"unknown command: {command!r}")

    return network
