# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
      st, res = [(-1,-1)], 0

      for i, h in enumerate(heights):
        while st[-1][1] >= h:
          _, curh = st.pop()
          res = max(res, curh * (i - 1 - st[-1][0]))
        st.append((i, h))
      
      for i in range(1, len(st)):
        res = max(res, st[i][1] * (len(heights) - 1 - st[i - 1][0]))
      return res