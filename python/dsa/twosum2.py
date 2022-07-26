class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # since array is sorted, we keep the right variable at end of array.
        # if sum of right and left is greater than target, we reduce right pointer by 1 so that we can come close to the target
        # as we know that reducing by 1 is only going to reduce the sum and result will come closer to target.
        # Likewise if sum is less than target, we increase the left pointer by 1.
        left, right = 0, len(numbers)-1

        while left < right:

            result = numbers[left] + numbers[right]

            if result == target:
                return [left+1, right+1]

            elif result > target:
                right = right - 1

            else:
                left = left + 1
