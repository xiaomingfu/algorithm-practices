# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_path = 0
        def dfs(node):
            if node is None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            nonlocal max_path
            max_path = max(l + r, max_path)
            return max(l, r) + 1
        dfs(root)
        return max_path

# second solution

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def h(node):
            if node is None:
                return 0
            return max(h(node.left), h(node.right)) + 1
        
        def dfs(node):
            if node is None:
                return 0
            return max(dfs(node.left), dfs(node.right),
            h(node.left) + h(node.right))
        return dfs(root)