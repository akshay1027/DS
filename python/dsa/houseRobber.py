class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        return self.helper(n-1, nums, dp)

    def helper(self, ind, nums, dp):
        if ind == 0:
            return nums[ind]

        if ind < 0:
            return 0

        if(dp[ind] != -1):
            return dp[ind]

        pick = nums[ind] + self.helper(ind - 2, nums, dp)
        notPick = 0 + self.helper(ind - 1, nums, dp)

        dp[ind] = max(pick, notPick)
        return dp[ind]
