from dataclasses import dataclass, field


@dataclass(frozen=True)
class Partner:
    """Represents a partner entity in the network."""

    name: str


@dataclass(frozen=True)
class Company:
    """Represents a company entity in the network."""

    name: str


@dataclass(frozen=True)
class Employee:
    """Represents an employee working for a specific company."""

    name: str
    company: str


@dataclass(frozen=True)
class Contact:
    """Represents a contact between an employee and a partner with a specific kind."""

    employee: str
    partner: str
    kind: str


@dataclass(frozen=True)
class Relationship:
    """Represents a relationship between a company and a partner with an associated score."""

    company: str
    partner: str | None
    score: int


# Represents allowed commands
Command = Partner | Company | Employee | Contact


@dataclass
class Network:
    """Represents the network of partners, companies, employees, and contacts."""

    partners: set[Partner] = field(default_factory=set)
    companies: set[Company] = field(default_factory=set)
    employees: dict[str, Employee] = field(default_factory=dict)
    contacts: list[Contact] = field(default_factory=list)
