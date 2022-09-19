class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        three, five = 3, 5

        for num in range(1, n+1):
            if num == three == five:
                ans.append("FizzBuzz")
                three += 3
                five += 5

            elif num == five:
                ans.append("Buzz")
                five += 5

            elif num == three:
                ans.append("Fizz")
                three += 3

            else:
                ans.append(str(num))

        return ans

    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        three, five = 3, 5

        for num in range(1, n+1):
            if num % 3 == 0 and num % 5 == 0:
                ans.append("FizzBuzz")

            elif num % 5 == 0:
                ans.append("Buzz")

            elif num % 3 == 0:
                ans.append("Fizz")

            else:
                ans.append(str(num))

        return ans
