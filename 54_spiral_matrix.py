# https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        i, j, res = 0, 0, []
        
        while m > 0 and n > 0:
            if m == 1:
                for k in range(n):
                    res.append(matrix[i][k + j])
            elif n == 1:
                for k in range(m):
                    res.append(matrix[i + k][j])
            else:
                for k in range(n - 1):
                    res.append(matrix[i][k + j])
                for k in range(m - 1):
                    res.append(matrix[i + k][n - 1 + j])
                for k in range(n - 1 + j, j, -1):
                    res.append(matrix[m - 1 + i][k])
                for k in range(m - 1 + i, i, -1):
                    res.append(matrix[k][j])
            m, n = m - 2, n - 2
            i, j = i + 1, j + 1
        return res
