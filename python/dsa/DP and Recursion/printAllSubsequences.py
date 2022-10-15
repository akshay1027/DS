def helper(i, ds, ans, str, n):
    if i == n:
        # print(ds)
        ans.append("".join(ds))
        return

    # pick
    ds.append(str[i])
    helper(i+1, ds, ans, str, n)
    ds.pop()

    # not pick
    helper(i+1, ds, ans, str, n)

    return ans


def subsequences(str):
    n = len(str)
    ans = []
    ds = []

    temp = helper(0, ds, ans, str, n)

    for str in temp:
        print(str, end=" ")


subsequences("abc")

# op: abc ab ac a bc b c
