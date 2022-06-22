# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        def bt(i, arr):
            if i == len(nums):
                res.append(arr[:])
            elif i < len(nums):
                arr.append(nums[i])
                bt(i + 1, arr)
                arr.pop()
                
                j = i
                while j < len(nums) and nums[i] == nums[j]:
                    j += 1
                bt(j, arr)
        bt(0, [])
        return res