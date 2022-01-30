# This is an input class. Do not edit.
from asyncio.windows_events import INFINITE
from json.encoder import INFINITY


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
  # left branch is strictly smaller than root, right branch is bigger or same as the root
  # root is the biggest in left branch, smallest in the right branch
  #O(n), O(d)
  def help(node, s, l):
    if not node:
      return True
    if not s <= node < l:
      return False
    left = help(node.left, s, node)
    right = help(node.right, node, l)
    return left and right
  help(tree, float('-inf'), float('inf'))