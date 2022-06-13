# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sort
        # nums.sort()
        # for i, n in enumerate(nums):
        #     if i != n:
        #         return i
        # return len(nums)
        
        
        # num_set = set(nums)
        # n = len(nums)
        # for i in range(n + 1):
        #     if i not in num_set:
        #         return i