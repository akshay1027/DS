class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for item in s:
            # get ithem from dict1, if not there, initilise with 0
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2

        # sorted is used for sorting strings.
        s = sorted(s)
        t = sorted(t)

        if s == t:
            return True

        return False
