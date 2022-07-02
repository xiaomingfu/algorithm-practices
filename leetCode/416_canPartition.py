# https://leetcode.com/problems/partition-equal-subset-sum/

from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        sub_sum = sum(nums) // 2
        @cache
        def dfs(i, remain):
            if remain == 0:
                return True
            if i < len(nums) and remain > 0:
                return dfs(i + 1, remain - nums[i]) or dfs(i + 1, remain)
        return dfs(0, sub_sum)