# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# 
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

# Example 1:
#
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        if n == 1:
            return [["Q"]]
        def canplace(row, col):
            if "Q" in board[row]:
                return False
            for i in range(n):
                if "Q" == board[i][col]:
                    return False
            dirs = [(-1,-1),(-1,1),(1,-1),(-1,-1)]
            r,c = row, col
            for dr, dc in dirs:
                r, c = r+dr,c+dc
                while (0<=r<n and 0<=c<n):
                    if board[r][c] == "Q":
                        return False
                    r, c = r+dr,c+dc
                r,c = row,col
            return True

        stack = []
        i = j = firstcol=  0
        res= []
        while i< n:
            rowqueen = False
            while j< n:
                if canplace(i,j):
                    board[i][j] = "Q"
                    stack.append((i,j))
                    rowqueen = True
                    if i == 0 and j> firstcol:
                        firstcol = j
                    break
                j+=1
            if rowqueen:
                i += 1
                if i == n:
                    res.append(["".join(board[r]) for r in range(n)])
                    r, c = stack.pop()
                    j = c+1
                    i = r
                    board[r][c] = "."
                else:
                    j = 0
            else:
                if not stack:
                    break
                i, j = stack.pop()
                board[i][j] = "."
                j += 1
        return res


s = Solution()
print("Expected Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]")
print("Actual Output: ", s.solveNQueens(4))
