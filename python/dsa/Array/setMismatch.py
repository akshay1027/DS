from collections import defaultdict


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n, withDuplicateSum, withoutDuplicateSum = len(
            nums), sum(nums), sum(set(nums))

        totalSum = n*(n+1)//2

        repeat = withDuplicateSum - withoutDuplicateSum
        loss = totalSum - withoutDuplicateSum
        return [repeat, loss]

    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = defaultdict(int)
        for x in nums:
            seen[x] += 1
        miss = dup = 0
        for i in range(1, n + 1):
            if i not in seen:
                miss = i
            elif seen[i] == 2:
                dup = i
        return [dup, miss]
