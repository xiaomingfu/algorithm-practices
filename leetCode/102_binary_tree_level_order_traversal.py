# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        f = [root]
        if not root:
            return res
        while len(f) > 0:
            res.append([n.val for n in f])
            q = []
            for n in f:
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            f = q        
        return res