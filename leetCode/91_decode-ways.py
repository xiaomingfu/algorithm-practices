# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        # f(i) = f(i - 1) + f(i - 2)
        @cache
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            res = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            return res            
        return dfs(0)

from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            res = dfs(i + 1)
            if i + 1 < len(s) and (10 < int(s[i:i+2]) <= 26):
                res += dfs(i + 2)
            return res
        return dfs(0)

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if s[0] == "0":
            dp[1] = 0
        else:
            dp[1] = 1
        for i in range(2,len(dp)):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            if 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]