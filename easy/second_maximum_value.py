"""
Implement a function findSecondMaximum(lst) which returns the second largest element in the list.

Input - [9,2,3,6]
Output - 6
"""

# Intuitive

def findSecondMaximum(lst):
    lst.sort(desc=True)
    return lst[2]

# Sorting can be costlier suppose the size of array is large, and also what if we have duplicates in
# the array , figure out something else

# Better

def findSecondMaximum_better(lst):
    max1, max2 = min(lst), min(lst)
    for i in lst:
        if i > max1:
            max2 = max1
            max1 = i
        else:
            if i > max2:
                max2 = i
    return max2





