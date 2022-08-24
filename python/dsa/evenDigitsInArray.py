class Solution:
    # print(~13 & 1) # op: 0
    # print(~12 & 1) # op: 1

    def findNumbers(self, nums: List[int]) -> int:

        res = 0
        for num in nums:
            print(~len(str(num)))
            if ~len(str(num)) & 1:
                res += 1

        return res

    def findNumbers1(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                res += 1

        return res

    def findNumbers2(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        for num in nums:
            while num > 0:
                num = int(num/10)
                count += 1

            if count % 2 == 0:
                ans += 1
            count = 0

        return ans
