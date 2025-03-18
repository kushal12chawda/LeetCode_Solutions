class Solution(object):
    def findMaxForm(self, strs, m, n):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            zeroes = s.count('0')
            ones = s.count('1')
            
            for i in range(m, zeroes - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeroes][j - ones])
        
        return dp[m][n]