import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax = -sys.maxsize - 1
        localMax = -sys.maxsize - 1
        n = len(nums)

        for r in range(n):
            localMax = localMax + nums[r]
            if nums[r] > localMax:
                localMax = nums[r]

            globalMax = max(globalMax, localMax)

        return globalMax
