https://leetcode.com/problems/sliding-window-maximum/

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
      q = deque()
      res = []

      for i, n in enumerate(nums):
        while q and q[-1][1] <= n:
          q.pop()
        q.append((i,n))
        if (i - q[0][0]) > k -1:
          q.popleft()
        if i >= k - 1:
          res.append(q[0][1])
      return res