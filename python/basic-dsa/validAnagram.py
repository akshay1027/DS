class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted is used for sorting strings.
        s = sorted(s)
        t = sorted(t)

        if s == t:
            return True

        return False
