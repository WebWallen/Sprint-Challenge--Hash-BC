#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    # Initialize Hashtable/ pass in the length(capacity), and assign to itinerary
    itinerary = HashTable(length)
    # Preallocate the route (array) memory by length/capacity
    route = [None] * length
    # For each ticket we have...
    for t in tickets:
        # Insert the itinerary (ht), source (key), and desination (value) in the hash table
        hash_table_insert(itinerary, t.source, t.destination)
    # Retrieve and assign the first ticket -- has destination, but no source (key or initial connecting flight)
    ticket = hash_table_retrieve(itinerary, "NONE")
    # While the ticket *does* have a destination on its key...
    while ticket != "NONE":
        # For each index in the range of our route array's length...
        for i in range(len(route)):
            # Assign each route's destination [value] to ticket, which places it inside the array
            route[i] = ticket
            # Call retrieve again on the same ticket's key to find the ticket with a matching source
            ticket = hash_table_retrieve(itinerary, ticket)
            # If the ticket doesn't have a destination...
            if ticket == "NONE":
                # Place at the end of our route
                route[i + 1] # have to increment because we aren't assining a value to ticket
                # Break out of the loop since work is done
                break
    # Return our newly organized route
    return route

tickets = [
  Ticket("NONE", "ORD"),
  Ticket("ORD", "CID"),
  Ticket("CID", "NONE"),
]

# Should print ORD, CID, NONE
print(reconstruct_trip(tickets, 3))