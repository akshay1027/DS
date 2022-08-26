class Solution:
    def getSum(self, a: int, b: int) -> int:

        # 32 bit converting by masking with hexadecimal

        # Sure. So the mask is used to handle the negative case. if there is no mask then this will be an #infinite loop, why?
        # If b is negative then MSB of 'b' is 1 and the loop "while b & mask != 0:" without mask will be an infinite #loop. So, the only reason of the mask is to handle the negative numbers.

        # This is even a better explanation(from where I understood how to handle to negative numbers): #https://leetcode.com/problems/sum-of-two-integers/discuss/84285/Understanding-the-mask-in-a-Python-#solution/88759
        mask = 0xffffffff

        while b & mask > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        if b > 0:
            return (a & mask)
        else:
            return a
