# Move the zeros to last of the sequence

# Exp :  1 2 0 3 0 4
#         :  1 2 3 4 0

# algorithm:
# 1) while getting input, count the number of zeros, dont append them in the array
# 2) sort the array
# 3) run a loop till total of zeros calculated in step 1 and append zeros in the array

num = []
count_zero = 0
n = int(input('enter the number of elements = '))

for i in range(0, n):
    ele = int(input())
    if ele == 0:
        count_zero += 1
    else:
        num.append(ele)

num.sort()

for i in range(0, count_zero):
    num.append(0)

print(num)
