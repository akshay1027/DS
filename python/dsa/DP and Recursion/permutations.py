class Solution:

    # 1st solution, using swapping
    def helper(self, ind, nums, ans):
        if ind == len(nums):
            ans.append(tuple(nums))
            return

        for i in range(ind, len(nums)):
            nums[ind], nums[i] = nums[i], nums[ind]
            self.helper(ind+1, nums, ans)
            nums[ind], nums[i] = nums[i], nums[ind]

        return ans

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        return self.helper(0, nums, ans)

    # 2nd solution, using hashmap and array ds to store
    def helper(self, nums, ds, hash, ans):
        if len(ds) == len(nums):
            ans.append(tuple(ds))
            return

        for i in range(len(nums)):
            if hash.get(nums[i], 0) == 0:
                hash[nums[i]] = 1
                ds.append(nums[i])
                self.helper(nums, ds, hash, ans)
                hash[nums[i]] = 0
                ds.pop()

        return ans

    def permute(self, nums: List[int]) -> List[List[int]]:
        hash = {}
        ds = []
        ans = []

        return self.helper(nums, ds, hash, ans)
