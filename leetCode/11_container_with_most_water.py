# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, hs: List[int]) -> int:
        maxS = float('-inf')
        for i in range(len(hs)):
            for j in range(i + 1, len(hs)):
                s = (j - i) * min((hs[j], hs[i]))
                maxS = max(s, maxS)
        return maxS

# second solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        maxS = float("-inf")
        while i < j:
            s = (j - i) * min(height[i], height[j])
            maxS = max(s, maxS)
            if height[j] < height[i]:
                j -= 1
            else:
                i += 1
        return maxS