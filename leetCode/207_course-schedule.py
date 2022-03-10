# https://leetcode.com/problems/course-schedule/
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      #construct graph
      dep_cnt, deps = defaultdict(int), defaultdict(set)
      for a, b in prerequisites:
        dep_cnt[a] += 1
        deps[b].add(a)
      
      #topological sort
      q = deque([n for n in range(numCourses) if dep_cnt[n] == 0])
      finished = set(q)
      while q:
        b = q.popleft()
        for a in deps[b]:
          dep_cnt[a] -= 1
          if dep_cnt[a] == 0:
            q.append(a)
            finished.add(a)
      return len(finished) == numCourses