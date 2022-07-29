# https://leetcode.com/problems/product-of-array-except-self/discuss/1597994/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Prefix-and-Suffix-product-O(1)-space-approach

class Solution:

    def productExceptSelf(self, nums):
        prod, zero_cnt = reduce(
            lambda a, b: a*(b if b else 1), nums, 1), nums.count(0)
        if zero_cnt > 1:
            return [0]*len(nums)
        for i, c in enumerate(nums):
            if zero_cnt:
                nums[i] = 0 if c else prod
            else:
                nums[i] = prod // c
        return nums

    #  my own solution
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # ip = [-1, 1, 0, 3, -3]
        # op = [0, 0, 9, 0, 0]
        # this example made me to use flag, count

        prod = 1
        flag = False  # using this to fidn out if there exists zero in array
        count = 0  # using this to find frequency of zeros, if its equal to 1, its an edge case

        for i, val in enumerate(nums):
            if val == 0:
                count += 1
                flag = True
                continue

            prod = val * prod

        # if no zero exists
        if not flag:
            for i in range(len(nums)):
                if prod == 0:
                    nums[i] = 0
                else:
                    nums[i] = prod // nums[i]
        # if zero exists, 2 cases -> 1 zero or more than 1 zero
        else:
            for i in range(len(nums)):
                if nums[i] == 0 and count == 1:
                    nums[i] = prod
                else:
                    nums[i] = 0

        return nums
