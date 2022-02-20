# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
      i, j = 0, len(s) - 1
      while i < j:
        a = s[i].lower()
        b = s[j].lower()
        if a == b:
          i, j = i + 1, j - 1
        elif not a.isalnum():
          i += 1
        elif not b.isalnum():
          j -= 1
        else:
          return False
      return True