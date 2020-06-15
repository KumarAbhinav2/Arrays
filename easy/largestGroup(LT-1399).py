"""
Given an integer n. Each number from 1 to n is grouped according to the sum of its digits.

Return how many groups have the largest size.

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.
"""
from collections import defaultdict


def largestGroup(num):
    # range given is 0 - 10000, max number is 9999 ...so total groups possible 36(9+9+9+9).
    mymap = defaultdict(list)
    def digitSum(n):
        s = 0
        while n:
            q, r = divmod(n, 10)
            s+=r
            n = q
        return s
    for i in range(1, num+1):
        mymap[digitSum(i)].append(i)
    max_size, max_groups = 0, 0
    for d_sum in mymap:
        curr_size = len(mymap[d_sum])
        if curr_size > max_size:
            max_size = curr_size
            max_groups = 1
        elif curr_size == max_size:
            max_groups +=1
    return max_groups


def countLargestGroup(n: int) -> int:
    dp = {0: 0}
    counts = [0] * (4 * 9)
    for i in range(1, n + 1):
        quotient, reminder = divmod(i, 10)
        dp[i] = reminder + dp[quotient]
        counts[dp[i] - 1] += 1
    return counts.count(max(counts))

largestGroup(13)








