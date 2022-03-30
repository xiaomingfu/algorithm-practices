# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use x, y to present position and i to present order for same cell node
        # use dictionary to store x, y, i, node info based on x as key
        # pre-order traversal
        
        dic = defaultdict(list)
        i = 0
        def dfs(node, x, y):
            nonlocal i
            if node:
                dfs(node.left, x - 1, y + 1)
                i += 1
                dic[x].append((y, i, node))
                dfs(node.right, x + 1, y + 1)
        dfs(root, 0, 0)
        res = []
        for k in sorted(dic.keys()):
            res.append([e[-1].val for e in sorted(dic[k])])
        return res
        