Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        avai_col = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
        avai_row = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
        avai_subsquare = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    avai_row[i].remove(val)
                    avai_col[j].remove(val)
                    avai_subsquare[(int(i/3)*3) + int(j/3)].remove(val)

        def backtrack(i, j, board):
            if board[i][j] != '.':
                if i == 8 and j == 8:
                    return True
                elif  j < 8:
                    return backtrack(i, j + 1, board)
                elif i < 8 and j == 8:
                    return backtrack(i + 1, 0, board)
            
            avai_set = avai_row[i] & avai_col[j] & avai_subsquare[(i//3)*3 + j//3]
            for v in avai_set:
                board[i][j] = str(v)

                avai_row[i].remove(v)
                avai_col[j].remove(v)
                avai_subsquare[(int(i/3)*3) + int(j/3)].remove(v)

                if (i == 8 and j == 8) or (j < 8 and backtrack(i, j + 1, board)) or (i < 8 and j == 8 and backtrack(i + 1, 0, board)):
                    return True

                board[i][j] = '.'
                avai_row[i].add(v)
                avai_col[j].add(v)
                avai_subsquare[(int(i/3)*3) + int(j/3)].add(v)

        backtrack(0, 0, board)

if __name__ == "__main__":
    s= Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print("""Expected Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]""")
    print("Actual Output:",s.solveSudoku(board))
