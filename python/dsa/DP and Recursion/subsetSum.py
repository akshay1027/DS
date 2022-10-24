def subsetSum(num, i, n, sum, ds):
    if i == n:
        ds.append(sum)
        return

    # pick/add
    subsetSum(num, i+1, n, sum + num[i], ds)

    # not pick/add
    subsetSum(num, i+1, n, sum, ds)

    return ds


# Driver Code
if __name__ == '__main__':

    num = [3, 1, 2]
    # s = []
    # s.append("abcadefgh")
    # s.append("xyzaq")
    ds = []
    sum = 0

    ans = subsetSum(num, 0, len(num), sum, ds)

    print(sorted(ans))

    # [0, 1, 2, 3, 3, 4, 5, 6]
