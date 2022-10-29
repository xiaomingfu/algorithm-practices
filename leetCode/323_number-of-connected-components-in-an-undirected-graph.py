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
# union-find: O(e)* ª(n)
        ids = list(range(n)) 
        cnt = n
        
        def find(p):
            if p != ids[p]:
                ids[p] = find(ids[p])
            return ids[p]
  
        def union(p, q):
            rp, rq = find(p), find(q)
            if rp != rq:
                ids[rq] = rp
                nonlocal cnt
                cnt -= 1
                
        for a, b in edges:
            union(a, b)
         
        return cnt
        # print(ids)
        # p = set()
        # for i in range(n):
        #     p.add(find(i))
        #     print(p)
        # return len(p)
