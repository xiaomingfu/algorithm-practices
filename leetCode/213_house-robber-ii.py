# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        # break the cirlce by delete the last one or first one
        # turn the question to f(k) = max(f(k - 1), f(n - 2) + nums[k])
        if len(nums) == 1:
            return nums[0]
        def helper(arr):
            if len(arr) == 0:
                return 0
            if len(arr) < 2:
                return arr[0]
            a, b = arr[0], max(arr[0], arr[1])
            for i in range(2, len(arr)):
                c = max(arr[i] + a, b)
                a, b = b, c
            return b
        return max(helper(nums[:len(nums) - 1]), helper(nums[1:]))