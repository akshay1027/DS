# https://leetcode.com/problems/longest-consecutive-sequence/discuss/1254566/Python-3-solutions-Clean-and-Concise

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSequence = 0

        for n in nums:
            if (n-1) not in numSet:
                currentSequence = 0
                while(n+currentSequence in numSet):
                    currentSequence += 1
                longestSequence = max(longestSequence, currentSequence)

        return longestSequence
