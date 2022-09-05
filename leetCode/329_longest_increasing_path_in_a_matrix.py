# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for i in range(m)]
        @cache
        def dfs(i, j):
            if not dp[i][j]:
                path = 0
                for a, b in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= a < m and 0 <= b < n and matrix[i][j] > matrix[a][b]:
                        path = max(path, dfs(a, b))
                dp[i][j] = 1 + path
            return dp[i][j]
            
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res
    