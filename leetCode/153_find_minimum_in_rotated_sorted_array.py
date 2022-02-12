# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        i = 0
        j = l - 1
        while i + 1 < j:
            if (nums[i] < nums[j]):
                return nums[i]
            m = (i + j) // 2
            if nums[i] < nums[m]:
                i = m + 1
            else:
                j = m
        return min(nums[i], nums[j])
        