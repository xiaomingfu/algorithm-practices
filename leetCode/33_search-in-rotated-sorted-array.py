# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        
        while i <= j:
            m = (i + j) // 2
            # check if i, j, m val is equal to target
            for k in [i, j, m]:
                if nums[k] == target:
                    return k
            # check three beside val
            if i + 2 >= j:
                return -1
            
            if nums[i] < nums[j]:
                if target > nums[m]:
                    i, j = m + 1, j - 1
                else:
                    i, j = i + 1, m - 1
            elif nums[i] < nums[m]:
                if nums[i] < target < nums[m]:
                    i, j = i + 1, m - 1
                else:
                    i, j = m + 1, j - 1
            else:
                if nums[m] < target < nums[j]:
                    i, j = m + 1, j - 1
                else:
                    i, j = i + 1, m - 1
        return -1