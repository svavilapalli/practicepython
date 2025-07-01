# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n*n in spiral order.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        row= col = 0
        dc = 'R'
        right = n
        bottom = n
        left = -1
        up = 0
        ans = [[0]*n for _ in range(n)]
        current = 1
        while up<=row<bottom and left <= col < right:
            if dc=='R' and col < right:
                for c in range(col, right):
                    ans[row][c] = current
                    current += 1
                dc = 'D' 
                right -= 1
                row+=1
                col = right
            if dc == 'D' and row < bottom:
                for r in range(row, bottom):
                    ans[r][col] = current
                    current += 1
                bottom -=1
                col-=1
                row= bottom
                dc= 'L'
            if dc == 'L' and col > left:
                for c in range(col, left,-1):
                    ans[row][c] = current
                    current+=1
                left += 1
                row -=1
                col = left
                dc = 'U'
            if  dc == 'U' and row > up:
                for r in range(row, up, -1):
                    ans[r][col] = current
                    current+=1
                up +=1
                col += 1
                row = up
                dc = 'R'
            if dc == 'R' and col >= right:
                break
            elif dc == 'U' and row <= up:
                break
            elif dc == 'L' and col <= left:
                break
            elif dc == 'D' and row >= bottom:
                break
        return ans


s = Solution()
n = 3
print("Expected Output: [[1,2,3],[8,9,4],[7,6,5]]")
print("Actual Output: ",s.generateMatrix(n))
