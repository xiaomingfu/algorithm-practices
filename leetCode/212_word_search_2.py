# https://leetcode.com/problems/word-search-ii/

class Trie_node:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie_node()
            cur = cur.children[c]
        cur.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # structure words in Trie
        root = Trie_node()
        for w in words:
            root.add_word(w)
         # dfs search word in board
        row, col = len(board), len(board[0])
        
        res, visited =set(), set()
        def dfs(i, j, node, str):
            if i < 0 or j < 0 or i == row or j == col or (i, j) in visited or board[i][j] not in node.children:
                return
            c = board[i][j]
            visited.add((i, j))
            node = node.children[c]
            str += c
            if node.is_word:
                res.add(str)
            # dfs check board in (x - 1), (x + 1), (y - 1), (y + 1) direction for word
            dfs(i + 1, j, node, str)
            dfs(i - 1, j, node, str)
            dfs(i, j + 1, node, str)
            dfs(i, j - 1, node, str)
            visited.remove((i, j))
        for x in range(row):
            for y in range(col):
                dfs(x, y, root, "")
        return list(res)
    