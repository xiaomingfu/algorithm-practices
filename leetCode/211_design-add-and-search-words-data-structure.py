# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Trie_node:
  def __init__(self):
    self.children = {}
    self.word = False


class WordDictionary:
  def __init__(self):
    self.root = Trie_node()
  
  def addWord(self, word:str) -> None:
    cur = self.root

    for c in word:
      if c not in cur.children:
        cur.children[c] = Trie_node()
      cur = cur.children[c]
    cur.word = True
  
  def search(self, word: str) -> bool:
    def dfs(j, root):
      cur = root
      for i in range(j, len(word)):
        c = word[i]
        if c == ".":
          # for all child in trie check match
          for child in cur.children.values():
            if dfs(i + 1, child):
              return True
          return False
        else:
          if c not in cur.children:
            return False
          cur = cur.children[c]
      return cur.word
    return dfs(0, self.root)