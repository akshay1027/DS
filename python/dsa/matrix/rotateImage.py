class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # [1, 2]
        # [3, 4]

        # [1, 3]
        # [2, 4]

        # [3, 1]
        # [4, 2]

        n = len(matrix)

        # matrix.reverse()

        # transpose the matrix
        for i in range(n):
            for j in range(i):
                # swap
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse each row
        for i in range(n):
            matrix[i].reverse()

        return matrix
