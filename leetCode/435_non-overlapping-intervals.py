# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
      # every intervals can be removed or kept, remove the least -> keep the most
        intervals.sort(key = lambda i: i[1])
        end = float("-inf")
        res = 0
        for s, e in intervals:
            if s >= end:
                res += 1
                end = e
        return len(intervals) - res
