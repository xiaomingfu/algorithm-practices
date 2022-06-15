https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
      res = []
      def isp(i, j):
        while i < j:
          if s[i] != s[j]:
            return False
          i, j = i + 1, j - 1
        return True

      def bt(i, arr):
        if i == len(s):
          res.append(arr[:])
        else:
          for j in range(i, len(s)):
            if isp(i, j):
              arr.append(s[i: j + 1])
              bt(j + 1, arr)
              arr.pop()
      bt(0, [])
      return res