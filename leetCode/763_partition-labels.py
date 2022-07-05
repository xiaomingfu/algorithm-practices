# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i, c in enumerate(s):
          d[c] = i
        
        res = []
        i, j, cur = 0, d[s[0]], 0
        while True:
          if cur == j:
            res.append(j - i + 1)
            i = j + 1
            if i > len(s) - 1:
              break
            j = d[s[i]]
          else:
            j = max(j, d[s[cur]])
          cur += 1
        return res