# https://leetcode.com/problems/interval-list-intersections/

# O(n^2, O(1))
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
#         intersection: max start, min end, and start smaller than end
        res = []
        len_f = len(firstList)
        len_s = len(secondList)
        for i in range(len_f):
            for j in range(len_s):
                f = max(firstList[i][0], secondList[j][0])
                l = min(firstList[i][1], secondList[j][1])
                if f <= l:
                    res.append([f, l])
        return res
    
# second solution two pointers
          res = []
          i, j = 0, 0
          while i < len_f and j < len_s:
            x, y = firstList[i]
            w, z = secondList[j]
            f = max(firstList[i][0], secondList[j][0])
            l = min(firstList[i][1], secondList[j][1])
            if f < l:
              res.append([f, l])
            if firstList[i][1] < secondList[j][1]:
              i += 1
            else:
              j += 1
          return res