# https://leetcode.com/problems/word-search-ii/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.widx = -1
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        # structure words in Trie
        root = TrieNode()
        for i, w in enumerate(words):
            node = root
            for c in w:
                idx = ord(c) - ord("a")
                if node.children[idx] is None:
                    node.children[idx] = TrieNode()
                node = node.children[idx]
            node.widx = i
        res = set()
        def dfs(i, j, node, visited):
            c = board[i][j]
            idx = ord(c) - ord("a")
            next_node = node.children[idx]
            if next_node is not None:
                if next_node.widx != -1:
                    res.add(words[next_node.widx])
                for a, b in [(i - 1, j), (i + 1, j), (i, j -1), (i, j + 1)]:
                    if 0 <= a < m and 0 <= b < n and (a, b) not in visited:
                        visited.add((a, b))
                        dfs(a, b, next_node, visited)
                        visited.remove((a, b))

        for i in range(m):
            for j in range(n):
                dfs(i, j, root, {(i, j)})
        return list(res)
    