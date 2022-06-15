# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def bt(i, arr, remain):
            if remain == 0:
                res.append(arr[:])
                
            else:
                if i < len(candidates) and remain >= 0:
                    n = candidates[i]
                    arr.append(n)
                    bt(i, arr, remain - n)
                    arr.pop()
                    bt(i + 1, arr, remain)
        
        bt(0, [], target)
        return res