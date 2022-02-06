# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = 0
        i = 0
        j = 0
        while j < len(s):
            k = s[j]
            if k not in dic:
                dic[k] = j
                j += 1
                res = max(res, j - i)
            else:
                t = dic[k]
                while i <= t:
                    del dic[s[i]]
                    i += 1
        return res