# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
      res = []
      def dfs(node):
        if node is None:
          res.append("#")
        else:
          res.append(str(node.val))
          dfs(node.left)
          dfs(node.right)

      dfs(root)
      " ".join(res)

    def deserialize(self, data):
      res = data.split()

      cur = 0
      def dfs():
        if res[cur] == "#":
          nonlocal cur
          cur += 1
          return None
        else:
          node = TreeNode(int(res[cur]))
          cur += 1
          node.left = dfs()
          node.right = dfs()
          return node
      return dfs()
