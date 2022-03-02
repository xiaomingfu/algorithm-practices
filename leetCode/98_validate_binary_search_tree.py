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
            if p < node.val < q:
                return dfs(node.left, p, node.val) and dfs(node.right, node.val, q)
            else:
                return False
        return dfs(root, float("-inf"), float("inf"))