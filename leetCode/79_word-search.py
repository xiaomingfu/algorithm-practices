# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(x, y, i, used):
            if i == len(word):
                return True
            for (a, b) in ((x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= a < m and 0 <= b < n and (a, b) not in used and board[a][b] == word[i]:
                    used.add((a, b))
                    if dfs(a, b, i + 1, used):
                        return True
                    used.remove((a, b))
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 1, {(i, j)}):
                    return True
        return False