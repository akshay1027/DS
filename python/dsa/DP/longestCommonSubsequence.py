from functools import lru_cache


# bottom up
class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        n1 = len(t1)
        n2 = len(t2)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if t1[i-1] == t2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[i][j]


# recursion + memoization
class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        n1 = len(t1)
        n2 = len(t2)
        # dp = [[-1]*(n2+1)]*(n1+1)
        dp = [[-1 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        return self.helper(n1-1, n2-1, t1, t2, dp)

    def helper(self, ind1, ind2, t1, t2, dp):
        if ind1 < 0 or ind2 < 0:
            return 0

        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        # if char match
        if t1[ind1] == t2[ind2]:
            dp[ind1][ind2] = 1 + self.helper(ind1-1, ind2-1, t1, t2, dp)

        else:
            # if char doesnot match
            dp[ind1][ind2] = max(self.helper(ind1, ind2-1, t1, t2, dp),
                                 self.helper(ind1-1, ind2, t1, t2, dp))
        return dp[ind1][ind2]

# class Solution:
#     def longestCommonSubsequence(self, t1: str, t2: str) -> int:
#         n1 = len(t1)
#         n2 = len(t2)

#         return self.helper(n1-1, n2-1, t1, t2)

#     @lru_cache(None)
#     def helper(self, ind1, ind2, t1, t2):

#         if ind1 < 0 or ind2 < 0:
#             return 0

#         # if char match
#         if t1[ind1] == t2[ind2]:
#             return 1 + self.helper(ind1-1, ind2-1, t1, t2)

#         # if char doesnot match
#         return max(self.helper(ind1, ind2-1, t1, t2),
#                    self.helper(ind1-1, ind2, t1, t2))
