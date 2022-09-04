class Solution:
    # wrong solution, my own
    def PredictTheWinner(self, nums: List[int]) -> bool:
        player1, player2 = 0, 0

        while len(nums):
            if len(nums) == 1:
                player1 = player1 + nums[0]
                nums.pop(0)

            elif len(nums) == 2:
                if nums[0] >= nums[1]:
                    player1 += nums[0]
                    player2 += nums[1]
                else:
                    player1 += nums[1]
                    player2 += nums[0]
                nums.pop(0)
                nums.pop(1)

            elif len(nums) == 3:
                if nums[0] >= nums[2] + nums[1]:
                    player1 += nums[0]

                    if nums[2] >= nums[1]:
                        player2 += nums[2]
                        nums.pop(2)
                    else:
                        player2 += nums[1]
                        nums.pop(1)
                    nums.pop(0)

                elif nums[2] > nums[0] + nums[1]:
                    player1 += nums[2]

                    if nums[0] >= nums[1]:
                        player2 += nums[0]
                        nums.pop(0)
                    else:
                        player2 += nums[1]
                        nums.pop(1)
                    nums.pop(2)

                elif nums[1] <= nums[0] + nums[2]:
                    player2 += nums[1]

                    if nums[0] >= nums[2]:
                        player1 += nums[0]
                        nums.pop(0)

                    else:
                        player1 += nums[2]
                        nums.pop(2)
                    nums.pop(1)

            # elif nums[0] >= nums[len(nums)-1]:
            elif nums[0] + nums[len(nums)-2] >= nums[len(nums)-1] + nums[1]:
                player1 += nums[0]
                player2 += nums[len(nums)-1]
                nums.pop(0)
                nums.pop(len(nums)-1)

            else:
                # nums[0] + nums[len(nums)-2] < nums[len(nums)-1] + nums[1]:
                player2 += nums[0]
                player1 += nums[len(nums)-1]
                nums.pop(0)
                nums.pop(len(nums)-1)

            # elif nums[0] <= nums[len(nums)-1]:

        if player1 > player2:
            return True
        else:
            return False
