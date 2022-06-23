https://leetcode.com/problems/binary-search/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = 0
        i, j = 0, len(nums) - 1
            
        while i <= j:
            m_idx = (i + j) // 2
            m = nums[m_idx]
            if m == target:
                return m_idx
            elif m < target:
                i = m_idx + 1
            else:
                j = m_idx - 1
        return -1