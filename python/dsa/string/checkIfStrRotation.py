# wont work if duplicate elements are there!
# def check1(s1, s2):

#     start = 0

#     for itr in range(len(s2)):
#         if s1[0] == s2[itr]:
#             start = itr
#             break

#     # start = 2
#     for itr in range(len(s1)):
#         if s1[itr] != s2[start]:
#             return False

#         if start == len(s1) - 1:
#             start = 0
#         else:
#             start += 1

#     return True


def check(s, goal):
    if (len(s) != len(goal)):
        return False

    q1 = []
    for i in range(len(s)):
        q1.append(s[i])

    q2 = []
    for i in range(len(goal)):
        q2.append(goal[i])

    k = len(goal)
    while (k > 0):
        ch = q2.pop(0)
        q2.append(ch)
        if (q2 == q1):
            return True

        k -= 1

    return False


# Driver Code
if __name__ == '__main__':

    s1 = "AACD"
    s2 = "ACDA"

    print(check(s1, s2))
