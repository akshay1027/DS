class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        dummy1 = [-1] * rows
        dummy2 = [-1] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dummy1[i], dummy2[j] = 0, 0

        for i in range(rows):
            for j in range(cols):
                if dummy1[i] == 0 or dummy2[j] == 0:
                    matrix[i][j] = 0

        return matrix
