class Solution(object):
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            row = [1] * (i + 1)
            result.append(row)
        
        for i in range(2, numRows):
            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        
        return result
        