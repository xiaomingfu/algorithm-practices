# https://leetcode.com/problems/last-stone-weight/

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
      for i in range(len(stones)):
        stones[i] *= -1
      heapq.heapify(stones)
      while len(stones) > 1:
        a = heapq.heappop(stones)
        b = heapq.heappop(stones)
        if a - b != 0:
          heapq.heappush(stones, a - b)
        
      return stones[-1] if len(stones) > 0 else 0
      