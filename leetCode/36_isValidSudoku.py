# https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # search n in row or col or sub-box
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sub_box = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row[i]:
                    return False
                else:
                    row[i].add(board[i][j])
                if board[i][j] in col[j]:
                    return False
                else:
                    col[j].add(board[i][j])
                k = (i // 3)*3 + j // 3
                if board[i][j] in sub_box[k]:
                    return False
                else:
                    sub_box[k].add(board[i][j])
        return True
                