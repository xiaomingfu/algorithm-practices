# https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      def can_finish_with_k(k):
        s = 0
        for p in piles:
          s += math.ceil(p / k)
          if s > h:
            return False
        return True

      l, r = 1, max(piles)
      while l < r:
        m = (l + r) // 2
        if can_finish_with_k(m):
          r = m
        else:
          l = m + 1
      return l