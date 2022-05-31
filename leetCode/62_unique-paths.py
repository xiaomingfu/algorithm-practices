# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      #f(i,j) = f(i - 1, j) + f(i, j - 1)
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

        dp = [[1] * n, [1] * n]
        for i in range(1, m):
            for j in range(1, n):
                dp[i % 2][j] = dp[(i - 1) % 2][j] + dp[i % 2][j - 1]
        return dp[(m -1) % 2][-1]
# top down
        @functools.cache
        def dp(x, y):
            if x == 0 or y == 0:
                return 1
            return dp(x - 1, y) + dp(x, y - 1)
        return dp(m-1, n-1)