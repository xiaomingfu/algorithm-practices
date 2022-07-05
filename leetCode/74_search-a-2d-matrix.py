# https://leetcode.com/problems/search-a-2d-matrix/

import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      m,n = len(matrix), len(matrix[0])
      i, j = 0, m - 1
      r = -1
      while i <= j:
        mid = (i + j) // 2
        if matrix[mid][0] > target:
          j = mid - 1
        elif matrix[mid][-1] < target:
          i = mid + 1
        else:
          r = mid
          break
      
      if r == -1:
        return False

      i = bisect.bisect_left(matrix[r], target)
      if i == n:
        return False
      if matrix[r][i] != target:
        return False
      return True