# https://leetcode.com/problems/number-of-1-bits/submissions/

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n != 0:
            if n & 1 == 1:  # check whether the last bit is 1
                cnt += 1
            n = int(n / 2)  # remove rightmost bit

            # n >> 2 # remove rightmost bit

        return cnt
