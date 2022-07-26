from collections import OrderedDict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        # max(count.values()) => will give maximum value present in hashmap count

        # left and right pointers to traverse across array
        left = 0

        # stores maximum character frequency in the window
        maxf = 0
        for right in range(len(s)):
            # count.get(s[index], 0) will check if s[index] exists in hashmap count, if not will add it with value 0
            count[s[right]] = 1 + count.get(s[right], 0)

            # set the maximum to max frequency of current character eventually you will get maxf.
            maxf = max(maxf, count[s[right]])

            if (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res
