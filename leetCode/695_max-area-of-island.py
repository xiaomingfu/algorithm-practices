# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        
        def bfs(i, j):
            cnt = 0
            q = [(i,j)]
            while q:
                new_q = []
                for i,j in q:
                    cnt += 1
                    for a, b in [(i - 1,j),(i + 1, j),(i, j - 1),(i, j + 1)]:
                        if 0 <= a < m and 0 <= b < n and (a, b) not in visited and grid[a][b] == 1:
                            new_q.append((a,b))
                            visited.add((a,b))
                q = new_q
            return cnt
        
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == 1:
                    visited.add((i,j))
                    res = max(res, bfs(i,j))
        return res