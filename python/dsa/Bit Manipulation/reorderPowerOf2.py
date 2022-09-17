class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        # instead of checking for all the combinations of number, we check for all the combinations of power of 2. That is we rearrage the question.

        if n > 0 and math.log(n, 2) == int(math.log(n, 2)):
            return True

        num = ''.join(sorted(str(n)))

        for i in range(0, 30):
            temp = ''.join(sorted(str(1 << i)))  # str(1 * pow(2, i))

            if num == temp:
                return True

        return False
