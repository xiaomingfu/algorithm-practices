https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(n, arr):
            if len(arr) == len(nums):
                res.append(arr[:])
            else:
                for i in range(len(n)):
                    arr.append(n[i])
                    bt(n[:i] + n[i + 1:], arr)
                    arr.pop()
        
        bt(nums, [])
        return res