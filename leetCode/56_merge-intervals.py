# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key= lambda i: i[0])
        for i in intervals:
            if len(res) > 0 and res[-1][1] >= i[0]:
                   res[-1][1] = max(res[-1][1], i[1])
            else:
                   res.append(i)
        return res