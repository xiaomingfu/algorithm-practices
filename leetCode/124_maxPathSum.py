# https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # max(left) + node + max(right) to update max_res
        # max(side) -> node.val + max(left) or max(right)
        
        max_res = float("-inf")
        
        def dfs(node):
            if node is None:
                return float("-inf")
            l, r = dfs(node.left), dfs(node.right)
            nonlocal max_res
            max_res = max(max_res, node.val + max(l, 0) + max(r, 0))
            return node.val + max(l, r, 0)
        dfs(root)
        return max_res