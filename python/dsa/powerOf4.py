import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n > 0 and math.log(n, 4) == int(math.log(n, 4)):
            return True
        else:
            return False
        # return math.log(n, 4) == int(math.log(n, 4)) if n > 0 else False
