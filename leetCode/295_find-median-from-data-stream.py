# https://leetcode.com/problems/find-median-from-data-stream/

import heapq
class MedianFinder:

    def __init__(self):
        self.min_h = []
        self.max_h = []

    def addNum(self, num: int) -> None:
      if not self.max_h or num <= -self.max_h[0]:
        heapq.heappush(self.max_h, -num)
      else:
        heapq.heappush(self.min_h, num)
      
      if len(self.max_h) > len(self.min_h) + 1:
        heapq.heappush(self.min_h, -heapq.heappop(self.max_h))
      elif len(self.min_h) > len(self.max_h):
        heapq.heappush(self.max_h, -heapq.heappop(self.min_h))
  
      def findMedian(self) -> float:
        if len(self.max_h) == len(self.min_h):
          return (-self.max_h[0] + self.min_h[0]) / 2.0
        else:
          return -self.max_h[0] * 1.0