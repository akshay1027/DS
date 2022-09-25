
from re import L


def helper(a):
    l = len(a)  # 9

    # i = 1 -> 8
    # j = 0
    # for i in range(1, l):
    #     if j <= len(a) - 1:
    #         if i != a[j]:
    #             return i
    #         j += 1

    # return i

    # i = 0 -> 6
    for i in range(0, l):
        if i+1 != a[i]:
            return i+1

    return i+2

    # Driver Code
if __name__ == '__main__':

    a = [1, 2, 3, 4, 5, 6, 7]

    print(helper(a))
