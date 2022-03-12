# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        # f(k) from (k + 1, nums[k] + 1), if f(j) reached last index return
        # chose the index which can reach fathest distance
        
        cnt = 0
        cur = 0
        if len(nums) < 2:
            return 0
        while True:
            cnt += 1
            if nums[cur] + cur + 1 >= len(nums):
                return cnt
            ns = cur
            for i in range(cur + 1, cur + nums[cur] + 1):
                if (nums[i] + i > nums[ns] + ns):
                    ns = i
            cur = ns