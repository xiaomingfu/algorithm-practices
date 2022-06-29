https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        i = 0
        for n in nums:
            heapq.heappush(h, n)
            if len(h) > k:
                heapq.heappop(h)
        return h[0]
            