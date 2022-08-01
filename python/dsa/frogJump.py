from typing import *
from xml.etree.ElementTree import indent

#inf = 10 ** 9


def helper(heights, ind, dp):
    if ind == 0:
        return 0

    if ind < 0:
        return 0

    if dp[ind] != -1:
        return dp[ind]

    # take1, take2 = inf, inf

    take1 = helper(heights, ind - 2, dp) + abs(heights[ind] - heights[ind - 2])
    take2 = helper(heights, ind - 1, dp) + abs(heights[ind] - heights[ind - 1])

    dp[ind] = min(take1, take2)
    # dp[ind]
    # print(ans)

    return dp[ind]


heights = [10, 20, 30, 10]
n = len(heights)
dp = [-1] * n
# n = n - 1
print(helper(heights, n - 1, dp))
