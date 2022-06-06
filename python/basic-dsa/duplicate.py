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
j = 0  # will contain the place where duplicate variable is available

for i in range(n):
    ele = int(input('ele = '))
    nums.append(ele)

# nums.sort()

# for i in range(1, len(nums)):
#     if nums[i] != nums[i-1]:
#         # print('nums of j = ', nums[j], ' ** nums of i = ', nums[i])
#         nums[j] = nums[i]
#         j += 1

# for i in range(j):
#     print(nums[i])

# solution 3:

# res = set(nums)
# print(res)

# solution 4: using hashmap
# Time complexity will be O(N) time and O(N) space
mp = {i: 'a' for i in nums}

for i in range(0, n):
    if mp[nums[i]] == 'a':
        nums[j] = nums[i]
        j = j+1
        mp[nums[i]] = 1

for i in range(j):
    print(nums[i])

# solution using hashmap

# hm = {i: 0 for i in nums}

# for i in range(0, len(nums)):
#     if hm[nums[i]] == 1:
#         return True
#     hm[nums[i]] = 1

# return False
