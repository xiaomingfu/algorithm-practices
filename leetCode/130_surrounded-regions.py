# https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # for "o" on the border and adjacent "o" put in a set
        # for "o" not in this set, turn into "x"
        visited = set()
        m, n = len(board), len(board[0])
        def helper(i, j):
            visited.add((i, j))
            for a, b in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= a < m and 0 <= b < n and board[a][b] == "O" and (a, b) not in visited:
                        helper(a, b)
        
        for i in range(m):
            for j in (0, n - 1):
                if board[i][j] == "O":
                    helper(i, j)
        for j in range(n):
            for i in (0, m - 1):
                if board[i][j] == "O":
                    helper(i, j)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"
        return board
        