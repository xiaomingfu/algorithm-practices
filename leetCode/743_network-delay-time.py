# https://leetcode.com/problems/network-delay-time/

from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        h = [(0, k)]
        completed = set()
        graph = defaultdict(list)
        for u, v, w in times:
          graph[u].append((w, v))
        while h:
          (dis, u) = heapq.heappop(h)
          if u not in completed:
            completed.add(u)
            if len(completed) == n:
              return dis
            for (w, v) in graph[u]:
              if v not in completed:
                heapq.heappush(h,(w + dis, v))
        return -1
          