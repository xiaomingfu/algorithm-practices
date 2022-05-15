# https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pre_t = -1
        n = len(position)
        for p, s in sorted(zip(position, speed), reverse=True):
            if (target - p) / s <= pre_t:
                n -= 1
            else:
                pre_t = (target - p) / s
        return n