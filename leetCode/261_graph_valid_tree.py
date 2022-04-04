# https://leetcode.com/problems/graph-valid-tree/

# graph is valid tree should meet n - 1 = len(edge)
# from root can tranvse all node, use seen(set)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        # restruct graph to dic
        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
    # use set to collection traverse node
        seen = set()
        def dfs(v):
            if v in seen:
                return 
            seen.add(v)
            for n in adj_list[v]:
                dfs(n)
        dfs(0)
        return len(seen) == n
