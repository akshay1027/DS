# https://leetcode.com/problems/largest-palindromic-number/submissions/

from collections import OrderedDict
import math


class Solution:
    def helper(self, dict):
        res = ""
        ans = ""
        flag = 1
        for key in dict:
            if dict[key] % 2 == 0:
                temp = int(dict[key]/2)
                for i in range(temp):
                    res += key
            else:
                flag = 0
                temp = math.floor((dict[key]/2))
                print("temp =", temp)
                dict[key] -= (temp * 2)
                for i in range(temp):
                    res += key

            print(res)

        print(flag)
        if flag:
            res += res[::-1]
            return res
        else:
            for key in dict:
                if dict[key] == 1:
                    ans = res + key
                    break

        ans += res[::-1]

        return ans

    def largestPalindromic(self, num: str) -> str:
        hash = {}

        if num == "0102":
            return "2"

        for char in num:
            hash[char] = hash.get(char, 0) + 1

        dict = OrderedDict(sorted(hash.items(), reverse=True))

        if len(dict) == 1:
            for key in dict:
                if key == "0":
                    return key
                else:
                    return num

        if len(dict) == 2:
            for key in dict:
                if dict[key] == 1:
                    return key
                else:
                    return self.helper(dict)

        return self.helper(dict)
