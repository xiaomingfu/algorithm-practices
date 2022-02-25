# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindromic(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True
    
        cnt = 0
        l = len(s)
        for i in range(l):
            for j in range(i, l):
                if isPalindromic(s[i:j + 1]):
                    cnt += 1
        return cnt
# second method, expand two pointer
        cnt = 0
        for i in range(len(s)):
            for j, k in [(i, i), (i, i + 1)]:
                while j >= 0 and k < len(s):
                    if s[j] == s[k]:
                        j, k = j - 1, k + 1
                        cnt += 1
                    else:
                        break
        return cnt