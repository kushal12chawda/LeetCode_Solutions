class Solution(object):
    def countSquares(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] and i > 0 and j > 0:
                    matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                count += matrix[i][j]

        return count