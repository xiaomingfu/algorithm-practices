# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @functools.cache
        def dp(x, y):
            if x == 0 or y == 0:
                return 1
            return dp(x - 1, y) + dp(x, y - 1)
        return dp(m-1, n-1)
  # second solution
        dp = [[1] * n for i in range(m)]
        print(dp)
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m-1][n-1]
        
