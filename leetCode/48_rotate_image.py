# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # swap left and right base middle
        # x, y => x, n - y - 1
        #swap right top to left bottom
        # x, y => n - y - 1, m - x - 1
        
        row = len(matrix)
        col = len(matrix[0])
        
        for i in range(row):
            for j in range(col // 2):
                matrix[i][j], matrix[i][col - 1 - j] = matrix[i][col - 1 - j], matrix[i][j]
        
        for i in range(row):
            for j in range(col - i):
                matrix[i][j], matrix[col - j - 1][row - i -1] = matrix[col - j - 1][row - i -1], matrix[i][j]
   