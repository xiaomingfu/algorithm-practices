# https://leetcode.com/problems/time-based-key-value-store/

from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.td = defaultdict(list)
        self.vd = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.td[key].append(timestamp)
        self.vd[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect_right(self.td[key], timestamp) - 1
        if i < 0:
          return ""
        return self.vd[key][i]