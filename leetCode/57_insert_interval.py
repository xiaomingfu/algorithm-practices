# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if merge, update newInterval
        # if not merge
        
        res = []
        for a, b in intervals:
          c, d = newInterval
            if a > d:
                res.append([c, d])
                c, d = a, b
            elif b < c:
                res.append([a, b])
            else:
                c, d = min(a, c), max(b, d)
        res.append([c, d])
        return res