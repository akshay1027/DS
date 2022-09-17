class Solution:
    def rob(self, nums: List[int]) -> int:
        nums1 = [0] * len(nums)
        nums2 = [0] * len(nums)

        n1 = len(nums) - 1
        n2 = len(nums)
        for i, j in zip(range(0, n2), range(1, n2)):
            if i == n1:
                nums2[i] = nums[j]
                break
            nums1[i], nums2[i] = nums[i], nums[j]

        # for i in range(len(nums) - 1):
        #     print(nums[i])
        #     nums1[i] = nums[i]

        # i = 0
        # for j in range(1, len(nums)):
        #     nums2[i] = nums[j]
        #     i += 1

        if len(nums) == 1:
            return nums[0]

        ans1 = self.rob1(nums1)
        ans2 = self.rob1(nums2)

        return max(ans1, ans2)

    def rob1(self, nums: List[int]) -> int:
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
