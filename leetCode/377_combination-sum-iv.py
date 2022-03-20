# https://leetcode.com/problems/combination-sum-iv/

from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
      # f(n) = sum(f(n - c) for c in coins)
      #f(0) = 1
      #f(-n) = 0
        @cache
        def dp(t):
            if t < 0:
                return 0
            elif t == 0:
                return 1
            else:
                return sum(dp(t - n) for n in nums)
        return dp(target)