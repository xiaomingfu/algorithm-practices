# https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ids = list(range(len(edges) + 1))
        
        def find(n):
            if n != ids[n]:
                n = find(ids[n])
            return ids[n]
        
        def union(a, b):
            a_p = find(a)
            b_p = find(b)
            if a_p != b_p:
                ids[b_p] = a_p
                
        for a, b in edges:
            a_p = find(a)
            b_p = find(b)
            if a_p != b_p:
                union(a,b)
            else:
                return [a,b]