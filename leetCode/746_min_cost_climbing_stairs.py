# https://leetcode.com/problems/min-cost-climbing-stairs/

from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dfs(i):
            if i <= 1:
                return 0
            
            return min(dfs(i - 1) + cost[i - 1], dfs(i - 2) + cost[i - 2])
        return dfs(len(cost))