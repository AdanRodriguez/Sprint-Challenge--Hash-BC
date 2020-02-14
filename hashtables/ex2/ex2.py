#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,)



class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = []

    """
    YOUR CODE HERE
    """

    # for loop - ticket in tickets (key: source, value: destination)
    for ticket in tickets:
        # hash table insert function ht, source, and destination
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # account for NONE
    destination = hash_table_retrieve(hashtable, 'NONE')
    # while loop - destination != NONE
    while destination is not 'NONE':
        # append destination to route
        route.append(destination)
        # destination set to retrieve ht, destination
        destination = hash_table_retrieve(hashtable, destination)

    # return route
    return route