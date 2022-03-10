# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      m, n = len(heights), len(heights[0])
      
      def bfs(front):
        res = set(front)
        while front:
          nf = []
          for a, b in front:
            for c, d in ((a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)):
              if 0 <= c < m and 0 <= d < n and heights[c][d] >= heights[a][b] and (c, d) not in res:
                  nf.append((c, d))
                  res.add((c, d))
          front = nf
        return res
    
      col = bfs([(0, j) for j in range(n)] + [(i, 0) for i in range(m)]) & bfs([(m - 1, j) for j in range(n)] + (i, n - 1) for i in range(m))
      return [list(e) for e in col]
