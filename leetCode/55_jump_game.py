# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reached = 0
        cur = 0
        while cur <= reached:
            reached = max(reached, nums[cur] + cur)
            if reached >= len(nums) - 1:
                return True
            cur += 1
        return False