# Given an m x n binary matrix mat, return the number of submatrices that have all ones.

# Example:
# Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
# Output: 13
# Explanation: 
# There are 6 rectangles of side 1x1.
# There are 2 rectangles of side 1x2.
# There are 3 rectangles of side 2x1.
# There is 1 rectangle of side 2x2. 
# There is 1 rectangle of side 3x1.
# Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        res = 0
        heights = [0] * cols
        for row in mat:
            for i in range(cols):
                if row[i] == 1:
                    heights[i] += 1
                else:
                    heights[i] = 0
            # histogram alg
            stack = []
            dp = [0] * cols
            for j in range(len(heights)):
                while stack and heights[j] <= heights[stack[-1]]:
                    stack.pop()

                if not stack:
                    dp[j] = heights[j] * (j+1)
                else:
                    top = stack[-1]
                    dp[j] = dp[top] + heights[j] * (j- top)
                stack.append(j)
                res += dp[j]
        return res


if __name__ == "__main__":
    mat = [[1,0,1],[1,1,0],[1,1,0]]
    s=Solution()
    print("Expected Output: 13")
    print("Actual Output:", s.numSubmat(mat))
