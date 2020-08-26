"""
Write a function that will take an array and print all the sub array with sum as 0

Input - [4, 2, -3, -1, 0, 4]
Output- [-3, -1, 0, 4], [0]

Input - [-1, -1, -1, -1]

Input - [6, 3, -1, -3, 4, -2, 2,
             4, 6, -12, -7]
"""

# Intuitive













def subArraySum_intuitive(arr):
    subsets = []
    for i in range(len(arr)):
        temp_arr = []
        my_sum = 0
        for j in range(i, len(arr)):
            temp_arr.append(arr[j])
            my_sum = my_sum + arr[j]
            if my_sum == 0:
                subsets.append(temp_arr.copy())
    return subsets


# [4, 2, -3, -1, 0, 4]
def subArraySum_better(arr):
    mymap = dict()  # Key as sum and values as list of indexes
    temp_sum = 0    # to hold sum
    result = []     # list of tuples (start and end index of sub arrays)
    for i in range(len(arr)):
        temp_sum += arr[i]
        if not temp_sum:     # if sum of list till this index results to 0 itself
            result.append((0, i))
        if temp_sum in mymap:
            for index in mymap[temp_sum]:
                result.append((index+1, i))
            mymap[temp_sum].append(i)
        else:
            mymap[temp_sum] = [i]
    for start,end in result:
        print(arr[start:end+1])


subArraySum_better([6, 3, -1, -3, 4, -2, 2,
             4, 6, -12, -7])










