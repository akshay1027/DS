class Solution:
    def subsetHelper(self, num, i, n, ans, ds):
        if i == n:
            ans.add(tuple(sorted(ds)))
            return

        # pick
        ds.append(num[i])
        self.subsetHelper(num, i+1, n, ans, ds)
        ds.pop()

        # not pick
        self.subsetHelper(num, i+1, n, ans, ds)

        return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = set()  # to avoid deplicate
        i = 0
        n = len(nums)
        ds = []

        return self.subsetHelper(nums, i, n, res, ds)

    # op:
    # [[1,2],[2],[1,2,3],[2,3],[1],[3],[],[1,3]]
