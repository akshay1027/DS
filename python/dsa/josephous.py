from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = deque(range(1, n+1))
        print(nums)
        while len(nums) > 1:
            # if arg inside rotate is negative value => shift in left, postive => shift in right
            nums.rotate(1-k)
            nums.popleft()
            # print(nums)
        return nums[0]

    def findTheWinner(self, n: int, k: int) -> int:
        setDs = sorted(set(range(1, n + 1)))
        print(setDs)
        idx = 0
        while len(setDs) > 1:
            idx = (idx + k - 1) % len(setDs)
            print(setDs)
            setDs.remove(setDs[idx])
        return setDs[0]

    def findTheWinner(self, n: int, k: int) -> int:
        hash = {x: x for x in range(1, n+1)}
        idx = 0
        while len(hash) > 1:
            idx = (idx + k - 1) % len(hash) + 1
            print(idx)
            hash.pop(idx)
        print(hash)
        return hash[idx]

    # my own approach
    def findTheWinner(self, n: int, k: int) -> int:
        while hash:
            if len(hash) == 1:
                return hash[i]

            if j == k:
                print(hash[i])
                j = 0
                hash.pop(i)

            j += 1
            if i == n:
                i = 1
            else:
                i += 1

                ls = list(range(1, n+1))
                k -= 1
                idx = k
                while len(ls) > 1:
                    ls.pop(idx)
                    idx = (idx + k) % len(ls)
                return ls[0]
