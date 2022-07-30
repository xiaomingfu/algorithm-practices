# https://leetcode.com/problems/swim-in-rising-water/
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        visited = set((0,0))
        h = [(grid[0][0], 0, 0)]
        
        while h:
            v, x, y = heapq.heappop(h)
            res = max(res, v)
            if x == n - 1 and y == n - 1:
                return res
            for a, b in [(x - 1, y), (x + 1, y),(x, y - 1),(x, y + 1)]:
                if 0 <= a < n and 0 <= b < n and (a, b) not in visited:
                    heapq.heappush(h,(grid[a][b], a, b))
                    visited.add((a,b))
                    