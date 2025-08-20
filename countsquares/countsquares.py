# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

# Example 1:

# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans=0
        r=len(matrix)
        c=len(matrix[0])
        maxx=0
        for dig in range(c):
            ans += matrix[0][dig]
        for dig in range(1,r):
            ans += matrix[dig][0]
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j] == 1 and matrix[i][j-1] > 0 and matrix[i-1][j] > 0 and matrix[i-1][j-1] > 0:
                    matrix[i][j] += min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])
                ans += matrix[i][j]
        return ans



if __name__== "__main__":
    s=Solution()
    matrix =[  [0,1,1,1],  [1,1,1,1],  [0,1,1,1]]
    print("Expected Output: 15")
    print("Actual Output:", s.countSquares(matrix))
