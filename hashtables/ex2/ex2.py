#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    sources = {}

    # Add destination airport to source airport in dict

    for ticket in tickets:
        sources[ticket.source] = ticket.destination
        print(sources)

    route = []
    item = "NONE"

    # Add each stop to flight route
    for x in range(len(tickets)):
        route.append(sources[item])
        item = sources[item]
        print(route)
    return route
