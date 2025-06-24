# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# 
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n ==1:
            return
        if n ==2:
            matrix[0][0],matrix[0][1],matrix[1][0],matrix[1][1] = matrix[1][0],matrix[0][0],matrix[1][1],matrix[0][1]
            return

        if n%2 == 0:
            rounds = n//2
        else:
            rounds = (n//2)+1
        r = 0
        l =n
        s = 0
        while s<l:
            left = top = s
            right = bottom = l-1
            for i in range(s,l-1):
                matrix[top][i],matrix[i][right],matrix[bottom][right-i+s],matrix[bottom-i+s][left] = matrix[bottom-i+s][left] ,matrix[top][i],matrix[i][right],matrix[bottom][right-i+s]
            s+=1
            l-=1


sl = Solution()
matrix = [[1,2,3,4,5,6,7,8,9,10],
[11,12,13,14,15,16,17,18,19,20],
[21,22,23,24,25,26,27,28,29,30],
[31,32,33,34,35,36,37,38,39,40],
[41,42,43,44,45,46,47,48,49,50],
[51,52,53,54,55,56,57,58,59,60],
[61,62,63,64,65,66,67,68,69,70],
[71,72,73,74,75,76,77,78,79,80],
[81,82,83,84,85,86,87,88,89,90],
[91,92,93,94,95,96,97,98,99,100]]
for r in matrix:
    print(r)
print("=================")
sl.rotate(matrix)
print("=================")
for r in matrix:
    print(r)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Expected Output: [[7,4,1],[8,5,2],[9,6,3]]")
sl.rotate(matrix)
print("Actual Output: ", matrix)
