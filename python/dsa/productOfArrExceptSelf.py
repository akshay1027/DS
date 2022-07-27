class Solution:
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

        if not flag:
            for i in range(len(nums)):
                if prod == 0:
                    nums[i] = 0
                else:
                    nums[i] = prod // nums[i]
        else:
            for i in range(len(nums)):
                if nums[i] == 0 and count == 1:
                    nums[i] = prod
                else:
                    nums[i] = 0

        return nums
