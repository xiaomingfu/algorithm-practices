# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def bfs(i, j):
            cnt = 0
            q = [(i,j)]
            while q:
                new_q = []
                for i,j in q:
                    cnt += 1
                    for a, b in [(i - 1,j),(i + 1, j),(i, j - 1),(i, j + 1)]:
                        if 0 <= a < m and 0 <= b < n and not visited[a][b] and grid[a][b] == 1:
                            new_q.append((a,b))
                            visited[a][b] = True
                q = new_q
            return cnt
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    visited[i][j] = True
                    res = max(res, bfs(i,j))
        return res