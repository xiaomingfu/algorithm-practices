# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q, cur_f = [], 0
        m, n = len(grid), len(grid[0])
        res = 0
        
        for i in range(m):
          for j in range(n):
            if grid[i][j] == 1:
              cur_f += 1
            if grid[i][j] == 2:
              q.append((i,j))
        if cur_f == 0:
          return 0
        while q:
          new_q = []
          res += 1
          for x, y in q:
            for a, b in ((x - 1, y), (x, y - 1),(x + 1, y), (x, y + 1)):
              if 0 <= a < m and 0 <= b < n and grid[a][b] == 1:
                grid[a][b] = 2
                new_q.append((a, b))
                cur_f -= 1
                if cur_f == 0:
                  return res
          q = new_q
        return -1