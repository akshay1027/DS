class Solution:
    def minPartitions(self, n: str) -> int:
        max = 0

        for i in range(len(n)):
            if int(n[i]) > max:
                max = int(n[i])

                if max == 9:
                    return max

        return max
