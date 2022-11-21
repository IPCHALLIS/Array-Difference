"""
This program implements a difference function.
It subtracts one list from another + returns the result.
It removes all values from list a, which are present in list b keeping their order.
If a value is present in b, all of its occurrences are removed from the other.
"""

import itertools

def array_diff(a, b):
    """This function subtracts list a from list b."""
    return(list(itertools.filterfalse(lambda x: x in b[:], a[:]))) # Use 'itertools.filterfalse' to return members of a, not in b.

print(array_diff([1,2],[1])) # should print [2]
print(array_diff([1,2,2,2,3],[2])) # should print [1,3]
print(array_diff([1,2,2], [])) # should print [1,2,2]
print(array_diff([1,2,2], [1])) # should print [2,2]
