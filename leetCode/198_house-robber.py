# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
#         f(k) = max(f(k - 1), f(k -  2) + nums[k])
        if len(nums) < 2:
            return nums[0]
        a = nums[0]
        b = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            c = max(b, a + nums[i])
            a, b = b, c
        return b