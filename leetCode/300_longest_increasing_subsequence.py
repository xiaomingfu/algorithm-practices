# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
       
    # second solution
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(i):
            res = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, helper(j) + 1)
            return res
        for i in range(n):
            return max(helper(i))