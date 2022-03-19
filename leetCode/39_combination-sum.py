# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dp(i, t, arr):
            if t == 0:
                res.append(arr[:])
            elif t < 0 or i >= len(candidates):
                return
            else:
                arr.append(candidates[i])
                dp(i, t - candidates[i], arr)
                arr.pop()
                dp(i + 1, t, arr)
        dp(0, target, [])
        return res