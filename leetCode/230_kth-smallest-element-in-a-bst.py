# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder tranverse BST
        
        res = root.val
        def dfs(node):
                if node is None:
                    return
                dfs(node.left)
                nonlocal k
                if k >= 1:
                    k -= 1
                    nonlocal res
                    res = node.val
                else:
                    return res
                dfs(node.right)
        dfs(root)
        return res
