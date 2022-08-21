from collections import defaultdict


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        occurrences, next_nums = defaultdict(int), defaultdict(int)
        # occurrence of every ele in array
        for num in nums:
            occurrences[num] += 1

        #occurences = {1:0, 2:0, 3:1, 4:2, 5:2}
        # nextNums = {3:0, 4:  6:1}
        for num in nums:
            # handles duplicates as well
            if occurrences[num] == 0:
                continue

            # If next_nums contains the number, it is directly appendable to a sequence.
            # We "append" it to the sequence by incrementing the next number by 1.
            elif next_nums[num] > 0:
                next_nums[num] -= 1
                next_nums[num + 1] += 1

            # If the number + 1 and the number + 2 are both still in the occurrences hashmap,
            # We can create a new subsequence of length 3 and add the next number to next_nums.
            elif occurrences[num + 1] > 0 and occurrences[num + 2] > 0:
                occurrences[num + 1] -= 1
                occurrences[num + 2] -= 1
                # minimum three numbers are formed. so we add the num + 4 (4th number) to next_nums
                next_nums[num + 3] += 1

            else:
                return False

            occurrences[num] -= 1
        return True
