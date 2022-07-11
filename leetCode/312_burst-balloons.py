# https://leetcode.com/problems/burst-balloons/
from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        @cache
        def dfs(i, j, l, r):
            res = 0
            if i > j:
                return 0
            for k in range(i, j + 1):
                res = max(res, dfs(i, k - 1, l, nums[k]), dfs(k + 1, j, nums[k], r), nums[k]*l*r)
            return res
        return dfs(0, len(nums) - 1, 1, 1)


      