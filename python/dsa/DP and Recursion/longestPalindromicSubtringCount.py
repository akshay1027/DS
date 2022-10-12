class Solution:
    def longestPalindrome(self, nums1: str) -> str:

        nums2 = nums1[::-1]
        n1 = len(nums1)
        n2 = n1

        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        ans = 0
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = 0

        return ans
