# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res = 0
        i = 0
        j = 0
        while j < len(s):
            c = s[j]
            if c not in seen:
                seen[c] = j
                j += 1
                res = max(res, j - i)
            else:
                temp = seen[c]
                while i <= temp:
                    del seen[s[i]]
                    i += 1
        return res