# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @functools.cache
        def dp(x, y):
            if x == 0 or y == 0:
                return 1
            return dp(x - 1, y) + dp(x, y - 1)
        return dp(m-1, n-1)