# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(None)
        def f(m):
          if m == 0:
            return 0
          res = float("inf")
          for c in coins:
            if m >= c:
              res = min(f(m - c) + 1, res)
          return res
    
        res = f(amount)
        if res == float("inf"):
          return -1
        return res