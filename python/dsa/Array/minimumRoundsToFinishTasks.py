from collections import Counter


class Solution:
    def minimumRounds(self, tasks) -> int:
        # Use Counter to get the frequency of each element
        tasks = [1, 1, 1, 2, 2, 2]
        count = Counter(tasks)
        print(count)
        c = 0  # to store the rounds
        for i in count:  # Loop through all the keys
            v = count[i]  # get the value of each key
            if v == 1:  # if v==1 then return -1 bcoz it is not posible to complete this task
                return -1
            while v % 3 != 0:  # Complete task in batch of 2 till total value is not divisible by 3.
                c += 1  # Increase count by 1
                v -= 2  # Decrease value by 2 as you are completing 2 tasks
            c += v//3  # When come out of the loop take quotient of val//3 to get rounds
        return c  # return the answer
