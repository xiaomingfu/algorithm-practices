# https://leetcode.com/problems/course-schedule-ii/

from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        deps = defaultdict(list)
        dep_cnt = defaultdict(int)
        q = []
        finished = []
        for a, b in prerequisites:
            deps[b].append(a)
            dep_cnt[a] += 1
        q = deque(n for n in range(numCourses) if not dep_cnt[n])
        finished = []
        while q:
            b = q.popleft()
            finished.append(b)
            for a in deps[b]:
                dep_cnt[a] -= 1
                if dep_cnt[a] == 0:
                    q.append(a)
        if len(finished) == numCourses:
            return finished
        return []