

# bottom up approach
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

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


# recursion + memoization
class Solution:
    class Sol:
        length = 0

    def helper(self, i1, i2, a1, a2, dp, ans):
        if i1 < 0 or i2 < 0:
            return 0

        if dp[i1][i2] != -1:
            return dp[i1][i2]

        #length = 0
        if a1[i1] == a2[i2]:
            dp[i1][i2] = 1 + self.helper(i1-1, i2-1, a1, a2, dp, ans)
            ans.length = max(ans.length, dp[i1][i2])

        self.helper(i1-1, i2, a1, a2, dp, ans)
        self.helper(i1, i2-1, a1, a2, dp, ans)

        #dp[i1][i2] = length

        return dp[i1][i2]

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        ans = self.Sol()

        dp = [[-1 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        self.helper(n1-1, n2-1, nums1, nums2, dp, ans)

        return ans.length
