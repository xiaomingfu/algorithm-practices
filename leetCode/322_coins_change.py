# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
      m = amount
      def f(m):
        res = float("inf")
        if m == 0:
          return 0
        for c in coins:
          if m >= c:
            res = min(res, f(m - c) + 1)
        return res
      
      res = f(m)
      if res == float("inf"):
        return -1
      return res