# correct solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        if goal == 0:
            return True
        else:
            return False


# wrong solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums) - 1

        localReach = nums[0]

        if length == 0:
            return True

        for r in range(length):

            if nums[nums[r] + r] == nums[length] or nums[localReach] == nums[length]:
                return True
            # if nums[nums[r]] == 0 and nums[localreach] == 0:
                # return False
            localReach = max(nums[localReach], nums[nums[r]])

        return False
