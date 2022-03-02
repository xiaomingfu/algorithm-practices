# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, p, q):
            if not node:
                return True
            if node.left and (node.val <= node.left.val or node.left.val <= q):
                return False
            if node.right and (node.val >= node.right.val or node.right.val >= p):
                return False
            return dfs(node.left, node.val, q) and dfs(node.right, p, node.val)
        return dfs(root, float("inf"), float("-inf"))