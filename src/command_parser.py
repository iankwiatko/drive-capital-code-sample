"""Parses text into a command list from the input text content and returns a list of command objects. splits content into individual lines via splitlines(), and then each line into tokens via split(). tokens are then matched against known command patterns to create corresponding command objects which will be used for building the network later. Also validates the input and raises errors for invalid lines or arguments."""

from .models import Command, Company, Contact, Employee, Partner


def parse_commands(content: str) -> list[Command]:
    command_list: list[Command] = []

    for line in content.splitlines():
        tokens = line.split()

        command, arguments = tokens[0], tokens[1:]
        match command, arguments:
            case "Partner", [name]:
                command_list.append(Partner(name))
            case "Company", [name]:
                command_list.append(Company(name))
            case "Employee", [name, company]:
                command_list.append(Employee(name, company))
            case "Contact", [employee, partner, kind]:
                # raise an error if the contact kind is not allowed
                if kind not in {"coffee", "call", "email"}:
                    raise ValueError(f"invalid contact kind {kind!r} on line: {line!r}")
                command_list.append(Contact(employee, partner, kind))
            case _:
                # raise an error for any unrecognized command
                raise ValueError(f"invalid input on line: {line!r}")

    return command_list
