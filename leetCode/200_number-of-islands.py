# https://leetcode.com/problems/number-of-islands/

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate grid, if grid[i][j] == 1, do dfs set val to 2, count how many not adjacent land
        
        m, n = len(grid), len(grid[0])
        cnt = 0
        
#         def dfs(i, j):
#             grid[i][j] == '2'
#             for a, b in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
#                 if 0 <= a < m and 0 <= b < n and grid[a][b] == "1":

#                     dfs(a, b)
        
    
        def bfs(i, j):
            f = deque([(i, j)])
            while f:
                for i, j in f:
                    grid[i][j] = "2"
                i, j = f.popleft()
                for a, b in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= a < m and 0 <= b < n and grid[a][b] == "1":
                        f.append((a, b))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    # dfs(i, j)
                    bfs(i, j)
        return cnt