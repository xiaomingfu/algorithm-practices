# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
            cnt = 0
            res = ""
            
            for i in range(len(s)):
                for j, k in [(i, i), (i, i + 1)]:
                    while j >= 0 and k < len(s):
                        if s[j] == s[k]:
                            l = k - j + 1
                            if l > cnt:
                                cnt = l
                                res = s[j: k + 1]
                        else:
                            break
                        j, k = j - 1, k + 1
            return res