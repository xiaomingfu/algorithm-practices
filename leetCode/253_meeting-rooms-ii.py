# https://leetcode.com/problems/meeting-rooms-ii/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        arr = []
        for s, e in intervals:
            arr.append((s, 1))
            arr.append((e, -1))
            res,  cnt = 0, 0
        for _, t in sorted(arr):
            cnt = cnt + t
            res = max(res, cnt)
        return res
            