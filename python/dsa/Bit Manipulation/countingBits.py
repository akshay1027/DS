class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            # print(type(bin(i))). returns binary form of num in str
            res.append(bin(i).count('1'))

        return res
