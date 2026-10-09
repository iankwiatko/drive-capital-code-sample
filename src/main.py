"""Responsible for orchestrating all functions."""

from .build_network import build_network
from .command_parser import parse_commands
from .format_relationships import format_relationships
from .input_loader import load_input
from .strongest_partners import strongest_partners


def main() -> None:
    content = load_input()
    commands = parse_commands(content)
    network = build_network(commands)
    relationships = strongest_partners(network)
    print(format_relationships(relationships))


if __name__ == "__main__":
    main()
