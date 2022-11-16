import sys

a1 = [1, 8, 7, 13]
a2 = [4, 17, 10, 0, -1]

a1 = sorted(a1)
a2 = sorted(a2)

l1 = len(a1)
l2 = len(a2)

res = sys.maxsize

i, j = 0, 0

while i < l1 and j < l2:
    if abs(a1[i] - a2[j]) < res:
        res = abs(a1[i] - a2[j])

    if a1[i] > a2[j]:
        j += 1
    else:
        i += 1

print(res)
