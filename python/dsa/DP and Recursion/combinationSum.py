class Solution:
    #ans = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.helper(candidates, target, [], ans, 0)
        return ans

    def helper(self, candidates, target, ds, ans, ind):
        if ind == len(candidates):
            if target == 0:
                ans.append(list(ds))
            return

        if(candidates[ind] <= target):
            ds.append(candidates[ind])
            self.helper(candidates, target - candidates[ind], ds, ans, ind)
            ds.pop(len(ds)-1)

        self.helper(candidates, target, ds, ans, ind+1)
