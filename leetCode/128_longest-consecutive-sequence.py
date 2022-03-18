# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # largest number and smallest number of the comsecutive sequence give the length of the sequence
        # pop set to get the element
        
        s = set(nums)
        res = 0
        while len(s) > 0:
            n = s.pop()
            l, r = n, n
            while l - 1 in s:
                l -= 1
                s.remove(l)
            while r + 1 in s:
                r += 1
                s.remove(r)
            res = max(res, r - l + 1)
        return res