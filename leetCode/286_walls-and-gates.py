# https://leetcode.com/problems/walls-and-gates/

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        
        q = []
        for x in range(m):
            for y in range(n):
                if rooms[x][y] == 0:
                    q.append((x, y))
        
        while q:
            new_q = []
            for a, b in q:
                for x, y in [(a - 1, b), (a + 1, b), (a, b - 1),(a, b + 1)]:
                    if 0<= x < m and 0 <= y < n and rooms[x][y] == 2147483647:
                        rooms[x][y] = rooms[a][b] + 1
                        new_q.append((x,y))
            q = new_q
        return rooms