# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
      def dfs(node):
        if node is None:
          return True, 0
        l_res, l_h = dfs(node.left)
        if not l_res:
          return False, 0
        r_res, r_h = dfs(node.right)
        return r_res and abs(r_h - l_h), max(l_h, r_h) + 1
      return dfs(root)[0]

      # second solution
        diff = 0
        def dfs(node):
            if node is None:
                return 0
            l_h = dfs(node.left) 
            r_h = dfs(node.right)
            nonlocal diff
            diff = max(abs(l_h - r_h), diff)
            return max(l_h, r_h) + 1
        dfs(root)
        return diff <= 1