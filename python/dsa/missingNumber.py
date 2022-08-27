class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # simplifying a^b^b =a
        # b^b -> 0
        # a^0 -> a
        xor = len(nums)

        for index in range(len(nums)):
            xor = xor ^ index ^ nums[index]

        return xor
