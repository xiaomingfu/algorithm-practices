class Node:

# Constructor to create a new node
  def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None
      self.parent = None

# A binary search tree 
class BinarySearchTree:

  # Constructor to create a new BST
  def __init__(self):
      self.root = None

  def find_largest_smaller_key(self, num):
    def dfs(node):
      if not node:
        return None
      if node.val >= num:
        return dfs(node.left)
      res = dfs(node.right)
      if not res:
        return node
      return res
    res = dfs(self.root)
    if not res:
      return -1
    else:
      return res.key

