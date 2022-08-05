class Solution:
    def firstElementKTime(self,  a, n, k):
        hash = {}

        for i in range(len(a)):
            if a[i] in hash:
                hash[a[i]] += 1
            else:
                hash[a[i]] = 1

            if hash[a[i]] == k:
                return a[i]

        return -1
