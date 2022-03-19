# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # scan from end to begin, till there is one match in the wordDict, k be the index devided s into two part,
        # if f(k) is true, then true
        words = set(wordDict)
        @functools.cache
        def dp(i):
            if i == 0:
                return True
            for j in range(i - 1, -1, -1):
                if s[j:i] in words and dp(j):
                    return True
            return False
        return dp(len(s))