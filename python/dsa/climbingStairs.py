# Making top-down not TLE using the lru_cache decorator.
# Basically the lru_cache decorator will automatically cache the result with the same method call argument,
# so climbStairs(x) will not be calculated more than once.
# The parameter of the decorator is the max_size for the cache,
# None means there is no size limit. This now will not TLE and beats 99.97%.

from functools import lru_cache


class Solution:
    @lru_cache(None)
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
