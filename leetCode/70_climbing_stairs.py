# https://leetcode.com/problems/climbing-stairs/

# O(n), O(n)
from functools import lru_cache
from sys import implementation


class Solution:
    def climbStairs(self, n: int) -> int:
      # fn = f(n - 1) + f(n - 2)
      #f(1) = 1
      #f(2) = 2
      @lru_cache(None)
      def f(k):
        if k <= 2:
           return k
        return f(k - 1) + f(k - 2)
      return f(n)

#second implement
    cache = {}
    def f(k):
      if k not in cache:
        if k <= 2:
          return k
        cache[k] = f(k - 1) + f(k -  2)
      return cache[k]
    
    return f(n)

#third implementation
    a, b = 1, 2
    for _ in range(n - 1):
      a, b = b, a + b
    return a
