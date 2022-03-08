# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        # top down
        @functools.cache
        def helper(i, j):
            if i == len(t1) or j == len(t2):
                return 0
            elif t1[i] == t2[j]:
                return 1 + helper(i + 1, j + 1)
            else:
                return max(helper(i + 1, j), helper(i, j + 1))
        return helper(0, 0)
        # bottom up
                m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]