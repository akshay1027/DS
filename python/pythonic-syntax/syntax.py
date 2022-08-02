
nums = [1, 2, 6, 3]

sorted(nums)  # sort in assending
sorted(nums, reverse=True)  # sort in dessending


# initiase map with values a for values(keys in dict) in nums
mp = {i: 'a' for i in nums}
print(mp)  # => {1: 'a', 2: 'a', 6: 'a', 3: 'a'}


# will give all elements in array except last one, => [1, 2, 6]
print(nums[:-1])
# will give all elements in array except last two, => [1, 2]
print(nums[:-2])
# will give elements in that range
print(nums[1:3])  # 2nd arg value will not be included, => [2, 6]


# running 2 variables in a loop simulaneously
n1, n2 = 2, 3
for i, j in zip(range(0, n2), range(1, n2)):
    pass

# but normally we prefer having just a pointer outside
j = 1
for i in range(0, n2):
    j += 1
    pass


count = {}
for right in range(len(nums)):
    # count.get(s[index], 0) will check if s[index] exists in hashmap count, if not will add it with value 0
    count[nums[right]] = 1 + count.get(nums[right], 0)


# nums[::-1] => will return reverse of nums, => [3, 6, 2, 1]
print(nums[::-1])


# sorted returns a list and sorted the hash in terms of values.
hash = {'a': 3, 'b': 1, 'c': 8, 'd': 6}
arr = sorted(hash, key=hash.get, reverse=True)
print(arr)  # ['c', 'd', 'a', 'b']


# create a 2D array
rows, cols = (2, 3)
arr = [[0]*cols]*rows
print(arr)  # [[0, 0, 0], [0, 0, 0]]
