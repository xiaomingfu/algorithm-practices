# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
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