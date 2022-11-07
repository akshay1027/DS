class Solution:

    # think of pascal s triangle as matrix
    def generate(self, numRows: int) -> List[List[int]]:

        res = [[1]*(i+1) for i in range(numRows)]

        #cols = 5
        #res1 = [[0]*cols for _ in range(numRows)]

        # j ranges from 1, i because last and first elements are always 1 in every column.

        for i in range(2, numRows):
            for j in range(1, i):

                res[i][j] = res[i-1][j-1] + res[i-1][j]

        return res
