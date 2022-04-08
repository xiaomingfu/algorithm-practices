# https://leetcode.com/problems/top-k-frequent-elements/
# solution 1: heap
from collections import Counter
from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count fequency
        cnt = Counter(nums)
        # heap
        h = []

        for n, feq in cnt.items():
            heappush(h, [feq, n])
            if len(h) > k:
                heappop(h)
        return [n[1] for n in h]

  # solution 2: busket sort

        cnt = Counter(nums)
        bsk = [[] for _ in range(len(nums) + 1)]

        for n, feq in cnt:
          bsk[feq].append(n)
        
        res = []
        for b in range(len(bsk) - 1, 0, -1):
          for n in b:
            res.append(n) 
            if len(res) == k:
              return res

