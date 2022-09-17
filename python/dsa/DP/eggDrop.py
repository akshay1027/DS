class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        def solve(e, f, dp):
            if (e, f) in dp:
                return dp[(e, f)]
            if f == 0 or f == 1:
                return f
            if e == 1:
                return f
            mn = 10**5  # max int
            for i in range(1, f+1):
                # ans = 1+max(break, not break)
                mn = min(mn, 1+max(solve(e-1, i-1, dp), solve(e, f-i, dp)))
            dp[(e, f)] = mn
            # print(dp)
            return mn
        return solve(k, n, {})
