import sys


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        a = sys.maxsize
        b = sys.maxsize
        for i in range(len(nums)):
            if nums[i] <= a:
                a = nums[i]

            elif nums[i] <= b:
                b = nums[i]

            else:
                return True

        return False
