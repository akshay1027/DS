class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxlen = 0
        unique = ['']

        for word in arr:
            for j in unique:
                tmp = word + j
                if len(tmp) == len(set(tmp)):
                    unique.append(tmp)
                    maxlen = max(maxlen, len(tmp))
        print(unique)
        return maxlen

    def maxLength(self, A):
        dp = [set()]
        for a in A:
            if len(set(a)) < len(a):
                continue
            a = set(a)
            for c in dp[:]:
                if a & c:
                    continue
                dp.append(a | c)
        return max(len(a) for a in dp)
