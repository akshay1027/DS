def helper(i, ds, ans, stri, n):
    if i == n:
        # print(ds)
        ans.append("".join(ds))
        return

    ds.append(stri[i])
    helper(i+1, ds, ans, stri, n)
    ds.pop()

    helper(i+1, ds, ans, stri, n)

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
