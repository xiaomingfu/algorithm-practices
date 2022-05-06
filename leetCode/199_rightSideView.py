# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = [root]
        while len(q) > 0:
            cur_q = []
            for n in q:
                if n.left:
                    cur_q.append(n.left)
                if n.right:
                    cur_q.append(n.right)
            res.append(q[-1].val)
            q = cur_q
        return res
