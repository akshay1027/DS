# Input:  { 2, 3, -7, 6, 8, 1, -10, 15 }
# [4, 3, 1, 2]
# [-4, -3]
# [2, 2, 4]
# []
# Output: 4

a1 = [-4, -3]
flag = 0
flag1 = 0
a1 = sorted(a1)

for i in range(len(a1)-1):
    if a1[i] > 0:
        flag1 = 1
        if a1[i+1] != a1[i] + 1 and a1[i] != a1[i+1]:
            flag = 1
            print(a1[i]+1)
            break
    # if i == len(a1) - 2:
    #     print(1)

if flag1 == 0:
    print(1)
    exit(0)

if flag == 0:
    print(a1[len(a1)-1] + 1)
