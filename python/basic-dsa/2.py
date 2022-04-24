# Move the zeros to last of the sequence

# Exp :  1 2 0 3 0 4
#         :  1 2 3 4 0

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
