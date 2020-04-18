"""
Implement a function, findFirstUnique(lst) that returns the first unique integer in the list.

Input - arr = [9,2,3,2,6,6]
output - 9
"""

# Intuitive way

def findfirstUnique_intuitive(lst):
    for i in range(len(lst)):
        if lst[i] in lst[i+1:]:
            continue
        return lst[i]











