#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    # for the index in the range of length
    for index in range(length):
        # set check weight to hash table retrieve `limit - weight`
        check_weight = hash_table_retrieve(ht, limit - weights[index])
        # check for None
        if check_weight is None:
            # then return hash table insert
            hash_table_insert(ht, weights[index], index)
        # otherwise
        else:
            # return the index, and weight check
            return (index, check_weight)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
