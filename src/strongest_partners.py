"""Determines the strongest partners for each company in the network based on the number of contacts and returns an ordered list of Relationship objects. Works by creating a Counter for each company, keeping track of connections to each partner. After counting connections, we iterate through all the companies, selecting the partner with the highest number of connections from each Counter, breaking ties alphabetically."""

from collections import Counter
from .models import Network, Relationship


def strongest_partners(network: Network) -> list[Relationship]:
    # create counter for each company that will hold partner connection counts
    totals: dict[str, Counter[str]] = {c.name: Counter() for c in network.companies}

    # iterate through all contacts and count connections for each partner
    for contact in network.contacts:
        company = network.employees[contact.employee].company
        totals[company][contact.partner] += 1

    # compile the strongest partner for each company
    results: list[Relationship] = []
    # first sort sorts by company names alphabetically
    for company in sorted(totals):
        connections = totals[company]
        best_partner = None
        best_count = 0
        # second sort helps to break ties alphabetically
        for partner in sorted(connections):
            count = connections[partner]
            if count > best_count:
                best_partner = partner
                best_count = count
        results.append(Relationship(company, best_partner, best_count))
    return results
