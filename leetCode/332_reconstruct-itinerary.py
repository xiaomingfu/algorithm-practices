# https://leetcode.com/problems/reconstruct-itinerary/
from collections import defaultdict, Counter

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
      # Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
      # Output: ["JFK","MUC","LHR","SFO","SJC"]

      # defaultdict(list)
      # sort
      # check used ticket
      g = defaultdict(list)
      for f, t in sorted(tickets):
        g[f].append(t)
      cnt = Counter(tuple(t) for t in tickets)

      def bt(f, cur):
          if len(cur) == len(tickets) + 1:
            return cur[:]
          for t in g[f]:
            if cnt[(f, t)] > 0:
              cur.append(t)
              cnt[(f, t)] -= 1
              res = bt(t, cur)
              if res:
                return res
              cnt[(f, t)] += 1
              cur.pop()
        
      bt("JFK", ["JFK"])