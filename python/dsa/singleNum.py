# https://leetcode.com/problems/single-number/
# xor operator of same number is 0
# xor operator of different number is 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res

        return res
