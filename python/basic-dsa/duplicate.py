# Solution 1:

# Time complexity will be O(NlogN) because we have used sorting.
# Space complexity will be O(N) using an extra array.

# n = int(input('Enter n= '))

# nums = []
# result = []

# for i in range(n):
#     ele = int(input('ele = '))
#     nums.append(ele)

# print('nums length = ', len(nums))
# nums.sort()

# result.append(nums[0])
# for i in range(len(nums)-1):
#     print("i", i)
#     if nums[i] != nums[i+1]:
#         result.append(nums[i+1])

# print(result)

# ==================================================================================

# solution 2:

# Time complexity will be O(NlogN) because we have used sorting.

n = int(input('Enter n= '))

nums = []
j = 1  # will contain the place where duplicate variable is available

for i in range(n):
    ele = int(input('ele = '))
    nums.append(ele)

nums.sort()

1, 1, 2, 4
for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
        print('nums of j = ', nums[j], ' ** nums of i = ', nums[i])
        nums[j] = nums[i]
        j += 1

for i in range(j):
    print(nums[i])
# print(nums)
