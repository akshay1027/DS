class Solution:
    def maxFrequencyOptimise(self, nums: List[int], k: int) -> int:
        i = 0
        nums.sort()
        for j in range(len(nums)):
            k += nums[j]
            if k < nums[j] * (j - i + 1):
                k -= nums[i]
                i += 1
        return j - i + 1

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            count = 1

            for j in range(i-1, -1, -1):
                if nums[j] == nums[i]:
                    count += 1
                    continue
                if k <= 0:
                    break
                temp = nums[j] + k
                if temp >= nums[i]:
                    dif = nums[i] - nums[j]
                    k -= dif
                    count += 1

            res = max(res, count)

        return res


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        tempK = k

        for i in range(len(nums) - 1, -1, -1):
            count = 1
            k = tempK

            for j in range(i-1, -1, -1):

                if k <= 0:
                    break

                if nums[j] + k >= nums[i]:
                    dif = nums[i] - nums[j]
                    k -= dif
                    count += 1

            res = max(res, count)

            if res > i:
                break

        return res


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        tempK = k

        for i in range(len(nums) - 1, -1, -1):
            count = 1
            a = nums[i]
            for j in range(i-1, -1, -1):

                if k > 0:
                    if a - nums[j] <= k:
                        k = k - (a - nums[j])
                        count = count + 1
                    else:
                        break

            k = tempK
            if count > res:
                res = count

            if res > i:
                break

        return res
