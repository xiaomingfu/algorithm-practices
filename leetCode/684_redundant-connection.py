# https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ids = list(range(len(edges) + 1))
        
        def find(n):
            # if n != ids[n]:
            #     n = find(ids[n])
            # return ids[n]

            # nodes = []
            # while n != ids[n]:
            #     nodes.append(n)
            #     n = ids[n]
            # r = n
            # for n in nodes:
            #     ids[n] = r
            # return r

            r = n
            while r != ids[r]:
                r = ids[r]
            while n != r:
                t = ids[n]
                ids[n] = r
                n = t
            return r

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