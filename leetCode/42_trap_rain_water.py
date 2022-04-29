# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        # find hightest idx, start -> hi, end-> hi
        # res += hi - cur_idx
        hi = height.index(max(height))
        res = 0
        for i in [range(0, hi), range(len(height) - 1, hi, -1)]:
            cur_h = 0
            for j in i:
                cur_h = max(height[j], cur_h)
                res = res + (cur_h - height[j])
        return res
        