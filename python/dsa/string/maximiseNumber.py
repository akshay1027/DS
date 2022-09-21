def maximizeNumber(num, k):
    num = str(num)
    l = len(num)
    res = ""

    for itr in range(l):
        if int(num[itr]) <= k and itr == 0:
            res = res + str(k) + num
            break

        elif int(num[itr]) <= k:
            res = res + str(k) + num[-(l-itr):]
            break

        elif int(num[itr]) > k:
            res += num[itr]
            if itr == l-1:
                res += str(k)

    return res


# Driver Code
if __name__ == "__main__":

    N = 77377
    K = 1
    print(maximizeNumber(N, K))
