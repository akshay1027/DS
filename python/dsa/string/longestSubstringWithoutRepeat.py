# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/347818/Python3%3A-sliding-window-O(N)-with-explanation

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        l = 0
        count = 0
        for r in range(0, len(s)):
            if s[r] not in map:
                count = max(count, r-l + 1)
            else:
                # if the character is outside window, we need not move the left pointer
                if map[s[r]] < l:
                    count = max(count, r-l + 1)

                # if the character is inside window, we move left pointer to next index after its value in
                else:
                    l = map[s[r]] + 1
            map[s[r]] = r

        return count


# Partially correct, but r wrote the logic ❤

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         map = {}
#         l = 1
#         globalCount = 1
#         localCount = 0
#         for r in range(0, len(s)-1):
#             #rint(s[r], s[l], s[r] not in map)
#             #rint(localCount, globalCount)
#             if s[r] != s[l] and s[r] not in map:
#                 map[s[r]] = 1
#                 localCount = localCount + 1
#             else:
#                 map.clear()
#                 globalCount = max(globalCount, localCount)
#                 localCount = 0
#             l = l + 1

#         return globalCount
