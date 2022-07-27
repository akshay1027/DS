
# python solution
# https://leetcode.com/problems/sum-of-two-integers/discuss/489210/Read-this-if-you-want-to-learn-about-masks

# c++ solution
# https://leetcode.com/problems/sum-of-two-integers/discuss/1394031/C%2B%2B-oror-100-faster-oror-With-explanation

class Solution:
    def getSum(self, a: int, b: int) -> int:

        # 32 bit converting by masking with hexadecimal
        mask = 0xffffffff

        while b & mask > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        if b > 0:
            return (a & mask)
        else:
            return a
