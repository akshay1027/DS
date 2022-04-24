# Check whether sum is equal to left and right of a no

# Exp 12345433

# Take 5 center
# 1+2+3+4 = 10
# 4+3+3= 10

nums = []
sumLeft = 0
sumRight = 0

n = int(input('Enter total number of elements = '))

for i in range(0, int(n/2)):
    ele = int(input("L = "))
    sumLeft += ele

for i in range(int(n/2), n):
    ele = int(input("R = "))
    sumRight += ele

print("Sum of left = ", sumLeft)
print("Sum of right = ", sumRight)
