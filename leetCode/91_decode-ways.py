# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        # f(i) = f(i + 1) + f(i + 2)
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
