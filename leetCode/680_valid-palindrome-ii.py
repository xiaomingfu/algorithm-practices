# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # delete either one and check whether remain is palindrome or not
        
        def helper(i, j):    
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True
    
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                if helper(i + 1, j) or helper(i, j - 1):
                    return True
                else:
                    return False
            else:
                i, j = i + 1, j - 1
        return True