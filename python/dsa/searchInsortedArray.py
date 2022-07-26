class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # target is in left sorted array
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1

                elif target < nums[mid] or target > nums[l]:
                    r = mid - 1

            # target is in right sorted array
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1

                elif target > nums[mid] or target < nums[r]:
                    l = mid + 1
        return -1
