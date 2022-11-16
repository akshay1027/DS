class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack)

    # TLE sol
    def removeDuplicates(self, s, k):
        s = list(s)
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= k and len(set(stack[-k:])) == 1:
                del stack[-k:]
        return "".join(stack)

    # My own solution, doesnot pass all test cases
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        j = k
        i = 0
        while i < len(s):
            k = j
            if stack and stack[-1] == s[i]:
                flag = 0
                k -= 2
                stack.append(s[i])
                while k != 0:
                    i += 1
                    if i < len(s) and stack[-1] == s[i]:
                        stack.append(s[i])
                        k -= 1
                    else:
                        flag = 1
                        break

                if flag == 0:
                    a = j
                    while a != 0:
                        a -= 1
                        stack.pop()

            else:
                stack.append(s[i])

            i += 1

        return "".join(stack)
