# Check whether sum is equal to left and right of a no

# Exp 12345433

# Take 5 center
# 1+2+3+4 = 10
# 4+3+3= 10

# algorithm:
# 1) take n
# 2) seperate [0 to n/2) and [n/2 to n) in a for loop using range method and add the values simultaneously

# note:
# 1) typecaste n/2 to int so that it wont be float value
# 2) the in range method of loop, the first value in paramater is inclunded and second value in parameter is not included while loopingk
# 3) use in range loop method for integers

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
