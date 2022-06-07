# https://leetcode.com/problems/longest-consecutive-sequence/discuss/1254566/Python-3-solutions-Clean-and-Concise

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSequence = 0

        for n in nums:
            if (n-1) not in numSet:
                countLocalSequence = 0
                while(n+countLocalSequence in numSet):
                    countLocalSequence += 1
                longestSequence = max(longestSequence, countLocalSequence)

        return longestSequence
