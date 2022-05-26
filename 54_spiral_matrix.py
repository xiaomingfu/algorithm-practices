# https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        up, down, l, r = 0, m - 1, 0, n - 1
        res = []
        while len(res) < m * n:
            for col in range(l, r + 1):
                res.append(matrix[up][col])
            for row in range(up + 1, down + 1):
                res.append(matrix[row][r])
            if up != down:
                for col in range(r - 1, l - 1, -1):
                    res.append(matrix[down][col])
            if l != r:
                for row in range(down - 1, up, -1):
                    res.append(matrix[row][l])
            up, down, l, r = up + 1, down - 1, l + 1, r - 1
        return res
        # m, n = len(matrix), len(matrix[0])
        # i, j, res = 0, 0, []
        
        # while m > 0 and n > 0:
        #     if m == 1:
        #         for k in range(n):
        #             res.append(matrix[i][k + j])
        #     elif n == 1:
        #         for k in range(m):
        #             res.append(matrix[i + k][j])
        #     else:
        #         for k in range(n - 1):
        #             res.append(matrix[i][k + j])
        #         for k in range(m - 1):
        #             res.append(matrix[i + k][n - 1 + j])
        #         for k in range(n - 1 + j, j, -1):
        #             res.append(matrix[m - 1 + i][k])
        #         for k in range(m - 1 + i, i, -1):
        #             res.append(matrix[k][j])
        #     m, n = m - 2, n - 2
        #     i, j = i + 1, j + 1
        # return res
