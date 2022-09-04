class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Power of 2 -> MSB of the number should be 1
        # Eg: n=8(1000b), n-1=7(0111b)
        # so n & (n-1) = 0
        if n > 0 and (n & (n-1)) == 0:
            return True
        else:
            False
