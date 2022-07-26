class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.AlphaNum(s[l]):
                l += 1
            while r > l and not self.AlphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l, r = l+1, r-1

        return True

    def AlphaNum(self, char):
        # ord returns ascii value of given parameter
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))

# extra space (newString variable) and reverse array also has extra space. Try to slove this problem in constant space!


class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""

        for char in s:
            if char.isalnum():
                newString += char.lower()

        # newString[::-1] => will return reverse of newString
        return newString == newString[::-1]


# my first solution
# import math
# import re

# class Solution:
    # newS = s.replace(" ", "")
    # pattern = re.compile('\W')
    # newStr = re.sub(pattern, '', newS)
    # newStr = newStr.lower()

    # n = math.ceil(len(newStr)/2)

    # left, right = 0, len(newStr) - 1

    # for left in range(n):
    #     if newStr[left] != newStr[right]:
    #         return False

    #     else:
    #         right -= 1

    # return True
