class Solution:

    def maxValueOptimise(self, n: str, x: int) -> str:
        if n[0] == '-':
            n = n[1:]
            for i in range(len(n)):
                if int(n[i]) > x:
                    n = n[:i] + str(x) + n[i:]
                    return "-" + n
                elif i == (len(n) - 1):
                    n = n + str(x)
                    return "-" + n

        else:
            for i in range(len(n)):
                if int(n[i]) < x:
                    n = n[:i] + str(x) + n[i:]
                    return n
                elif i == (len(n) - 1):
                    n = n + str(x)
                    return n

    def maxValue(self, n: str, k: int) -> str:
        num = n
        l = len(n)
        n = int(n)
        res = ""

        if n >= 0:
            for itr in range(l):
                if int(num[itr]) < k:
                    res = res + str(k) + num[-(l-itr):]
                    break

                elif int(num[itr]) >= k:
                    res += num[itr]
                    if itr == l-1:
                        res += str(k)
        else:
            res += '-'
            for itr in range(1, l):
                if int(num[itr]) <= k:
                    res += num[itr]
                    if itr == l-1:
                        res += str(k)

                elif int(num[itr]) > k:
                    res = res + str(k) + num[-(l-itr):]
                    break

        return res
