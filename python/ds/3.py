# Print array in interchange format
# Exp :
# Arr1 = [ 1,2,3,4,5]
# Arr2 = [ 7,8,9]
# Output = [ 1,7,2,8,3,9,4,5]

nums1 = []
nums2 = []
result = []
flag = 0

n1 = int(input('Enter total number of elements in 1 = '))
n2 = int(input('Enter total number of elements in 2 = '))

if n1 > n2:
    n = n2
    flag = 1
elif n1 < n2:
    n = n1
    flag = 2
else:
    n = n1

for i in range(0, n1):
    ele = int(input())
    nums1.append(ele)

for i in range(0, n2):
    ele = int(input())
    nums2.append(ele)

print("n = ", n)
for i in range(0, n):
    result.append(nums1[i])
    result.append(nums2[i])

if flag == 1:
    for i in range(n, n1):
        result.append(nums1[i])

elif flag == 2:
    for i in range(n, n2):
        result.append(nums2[i])

print(result)
