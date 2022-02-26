# https://leetcode.com/problems/set-matrix-zeroes/

#O(n^m) O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
#         store value = 0, index = (i, j), j in first row, i in first col
#         check first row and first col with 0 value
#         ture position with same i in first col or same j in first row to 0
        m = len(matrix)
        n = len(matrix[0])
        r0 = False
        c0 = False
        
        for j in range(n):
            if matrix[0][j] == 0:
                r0 = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                c0 = True
                break
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        for y in range(1, n):
            if matrix[0][y] == 0:
                for x in range(1, m):
                    matrix[x][y] = 0
                    
        for x in range(1, m):
            if matrix[x][0] == 0:
                for y in range(1, n):
                    matrix[x][y] = 0
        if r0:
            for j in range(n):
                matrix[0][j] = 0
        if c0:
            for i in range(m):
                matrix[i][0] = 0      
                

# second solution
#O(n^2) O(m + n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rs = set()
        cs = set()
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rs.add(i)
                    cs.add(j)
                    
        for x in rs:
            for y in range(n):
                matrix[x][y] = 0
        for y in cs:
            for x in range(m):
                matrix[x][y] = 0
        