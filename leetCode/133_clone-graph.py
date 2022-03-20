# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mapping = {}
        if node is None:
            return None
        def dfs(node):
            if node not in mapping:
                new_node = Node(node.val)
                mapping[node] = new_node
                new_node.neighbors = [dfs(n) for n in node.neighbors]
            return mapping[node]
        return dfs(node)