# https://leetcode.com/problems/task-scheduler/

from collections import Counter
import heapq
class Solution:
  def leastInterval(self, tasks: List[str], n: int) -> int:
    h = []
    res = 0
    for k, v in Counter(tasks).items():
      heapq.heappush(h, (-v, k))
    while h:
      newh = []
      for _ in range(n + 1):
        res += 1
        if h:
          v, k = heapq.heappop(h)
          if v != -1:
            newh.append((v + 1, k))
        if not h and not newh:
          break
      for v, k in newh:
        heapq.heappush(h, (v, k))
    return res 