# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # rebuilt graph in dic
        dic = defaultdict(list)

        for a, b in edges:
            dic[a].append(b)
            dic[b].append(a)
        # tranverse node in graph
        cnt = 0
        visited = []
        def dfs(v):
            for e in dic[v]:
                if e not in visited:
                    visited.append(e)
                    dfs(e)
        # store not visited node in arr, and count
        for v in range(n):
            if v not in visited:
                visited.append(v)
                cnt += 1
                dfs(v)
        return cnt
