# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # inorder -> first root then left last right
        # preorder => first left then root last right
        
        def dfs(P, I):
            if len(P) == 0:
                return None
            v = P[0]
            root = TreeNode(v)
            i = I.index(v)
            root.left = dfs(P[1: i + 1], I[:i])
            root.right = dfs(P[i+1:], I[i + 1:])
            return root
        return dfs(preorder, inorder)
 