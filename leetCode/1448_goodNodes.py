# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, cur):
            if node is None:
                return
            if node.val >= cur:
                nonlocal res
                res += 1
            dfs(node.left, max(node.val, cur))
            dfs(node.right, max(node.val, cur))
        dfs(root, root.val)
        return res