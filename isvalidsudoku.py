# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# 
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# 
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validrows = [[False]*9 for _ in range(9)]
        validcols = [[False]*9 for _ in range(9)]
        validblocks = [[False]*9 for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    val = int(board[row][col])-1
                    if validrows[row][val] or validcols[col][val] or validblocks[(row//3)*3 + col//3][val] :
                        return False
                    validrows[row][val] = True
                    validcols[col][val] = True
                    validblocks[(row//3)*3 + col//3][val] = True
        return True


s = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print("Expected Output : True")
print("Actual Output : ",s.isValidSudoku(board))
