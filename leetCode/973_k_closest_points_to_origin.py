https://leetcode.com/problems/k-closest-points-to-origin/
import heapq
class Solution:
  def kClosest(self, points:List[List[int]],k:int) -> List[List[int]]:
    h = []
    for i, (x, y) in enumerate(points):
      heapq.heappush(h,(-(x*x + y*y), i))
      if len(h) > k:
        heapq.heappop(h)
    return [points[i] for _, i in h]