# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie_node:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = Trie_node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            v = ord(c) - ord("a")
            if not node.children[v]:
                node.children[v] = Trie_node()
            node = node.children[v]
        node.is_word = True
                
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            v = ord(c) - ord("a")
            if not node.children[v]:
                return False
            node = node.children[v]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            v = ord(c) - ord("a")
            if not node.children[v]:
                return False
            node = node.children[v]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
