class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        if t == "":
            return False

        l1 = len(s)
        i = 0

        for char in t:
            if s[i] == char:
                i += 1
            if i == l1:
                return True

        return False
