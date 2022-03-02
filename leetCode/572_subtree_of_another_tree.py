# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return is_same(p.left, q.left) and is_same(p.right, q.right)
        
        # iterate every node in tree
        def dfs(node):
            if node:
                if is_same(node, subRoot):
                    return True
                return dfs(node.left) or dfs(node.right)
            return False
        return dfs(root)