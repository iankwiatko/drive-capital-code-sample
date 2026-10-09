"""Formats a list of Relationship objects into a pretty-printed string."""

from .models import Relationship


def format_relationships(relationships: list[Relationship]) -> str:
    output = []
    for relationship in relationships:
        if relationship.partner is None:
            detail = "No current relationship"
        else:
            detail = f"{relationship.partner} ({relationship.score})"
        output.append(f"{relationship.company}: {detail}")
    return "\n".join(output)
