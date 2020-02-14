#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    # Initialize hashtable and set its capacity
    ht = HashTable(16)
    # For the first weight in the range from 0 to length...
    for weight_1 in range (0, length):
        # Insert the hashtable, [weight key], and weight value
        hash_table_insert(ht, weights[weight_1], weight_1)
    # For the second weight in the range from 0 to length...
    for weight_2 in range (0, length):
        # Subtract weight 2 value from limit and assign result to matching_weight
        matching_weight = limit - weights[weight_2]
        # Retrieve the matching weight from hash table and assign to found_weight
        found_weight = hash_table_retrieve(ht, matching_weight)
        # If we found a weight...
        if found_weight:
            # Return the found weight and its partner weight_2
            return(found_weight, weight_2) 
    # Return None (means no matching weight was found)
    return None

test_weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
matching_weights = get_indices_of_item_weights(test_weights, 10, 11)
# Should return 9, 0 (10 + 1 = 11)
print(matching_weights)

# def print_answer(answer):
#     if answer is not None:
#         print(str(answer[0] + " " + answer[1]))
#     else:
#         print("None")