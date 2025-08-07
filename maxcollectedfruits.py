# There is a game dungeon comprised of n x n rooms arranged in a grid.

# You are given a 2D array fruits of size n x n, where fruits[i][j] represents the number of fruits in the room (i, j). Three children will play in the game dungeon, with initial positions at the corner rooms (0, 0), (0, n - 1), and (n - 1, 0).

# The children will make exactly n - 1 moves according to the following rules to reach the room (n - 1, n - 1):

# The child starting from (0, 0) must move from their current room (i, j) to one of the rooms (i + 1, j + 1), (i + 1, j), and (i, j + 1) if the target room exists.
# The child starting from (0, n - 1) must move from their current room (i, j) to one of the rooms (i + 1, j - 1), (i + 1, j), and (i + 1, j + 1) if the target room exists.
# The child starting from (n - 1, 0) must move from their current room (i, j) to one of the rooms (i - 1, j + 1), (i, j + 1), and (i + 1, j + 1) if the target room exists.
# When a child enters a room, they will collect all the fruits there. If two or more children enter the same room, only one child will collect the fruits, and the room will be emptied after they leave.

# Return the maximum number of fruits the children can collect from the dungeon.

 

# Example:

# Input: fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]

# Output: 100

# Explanation:

# In this example:

# The 1st child (green) moves on the path (0,0) -> (1,1) -> (2,2) -> (3, 3).
# The 2nd child (red) moves on the path (0,3) -> (1,2) -> (2,3) -> (3, 3).
# The 3rd child (blue) moves on the path (3,0) -> (3,1) -> (3,2) -> (3, 3).
# In total they collect 1 + 6 + 11 + 16 + 4 + 8 + 12 + 13 + 14 + 15 = 100 fruits.


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        
        n = len(fruits)
        if n==0:
            return 0
        i2 = 0
        j2 = n-1
        i3 = n-1
        j3 =0
        dp1 = [0]*n
        dp2 = [[(0,0,0)] for _ in range(n)]
        dp3 = [[(0,0,0)] for _ in range(n)]
        dp1[0] = fruits[0][0]
        dp2[0] = [(fruits[i2][j2], i2, j2)]
        dp3[0] = [(fruits[i3][j3], i3, j3)]
        dp = [[0]*n for _ in range(n)]
        dp[0][0] = fruits[0][0]
        dp[0][n-1] = fruits[0][n-1]
        dp[n-1][0] = fruits[n-1][0]
        nextrow = 2
        for i in range(1,n-1):
            dp[i][i] = dp[i-1][i-1]+fruits[i][i]
            j= n-1
            while j>=j2-1:
                if j<= i:
                    break
                dp[i][j]=max(dp[i-1][j-1:j+2])+fruits[i][j]

                dp[j][i] = max([dp[j-1][i-1],dp[j][i-1],dp[j+1 if j<n-1 else j][i-1]])+fruits[j][i]
                j-=1
            if j2-1 <= i:
                j2 += 1
            else:
                j2 -= 1
        
        return fruits[n-1][n-1]+dp[n-2][n-2]+dp[n-2][n-1]+dp[n-1][n-2]

if __name__ == "__main__":
    s = Solution()
    fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]
    print("Expected Output: 100")
    print("Actual Output: ",s.maxCollectedFruits(fruits))
