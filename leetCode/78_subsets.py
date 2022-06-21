# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def bt(i, cur):
            if i == len(nums):
                res.append(cur[:])
            elif i < len(nums):
                cur.append(nums[i])
                bt(i + 1, cur)
                cur.pop()
                bt(i + 1, cur)
        bt(0,[])
        return res