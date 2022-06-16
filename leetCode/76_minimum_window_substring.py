https://leetcode.com/problems/minimum-window-substring/

from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
      sd = defaultdict(int)
      td = Counter(t)
      i, j = 0, 0
      l, r = -1, len(s)

      def contain_all():
        for k, v in td.items():
          if sd[k] < v:
            return False
        return True
        
      while True:
        if contain_all():
          c = s[i]
          if r - l > j - i:
            l, r = i, j
          sd[c] -= 1
          i += 1
        else:
          if j == len(s):
            break
          c = s[j]
          sd[c] += 1
          j += 1

      if l == -1:
        return ""
      return s[l:r]