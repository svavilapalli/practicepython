# You are given an n x n square matrix of integers grid. Return the matrix such that:

# The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
# The diagonals in the top-right triangle are sorted in non-decreasing order.
 

# Example:
# Input: grid = [[1,7,3],[9,8,2],[4,5,6]]
# Output: [[8,2,3],[9,6,7],[4,5,1]]


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        if n == 1:
            return grid
        diagonals = [[] for _ in range(n+n-1)]
        for i,j in product(range(n), range(n)):
            v = n+j-i-1
            diagonals[v].append(grid[i][j])
        for i,d in enumerate(diagonals):
            d.sort(reverse= True if i<n else False)
        for i,j in product(range(n), range(n)):
            v = n+j-i-1
            val = diagonals[v][0]
            del diagonals[v][0]
            grid[i][j] = val
        return grid


if __name__ == "__main__":
    s=Solution()
    grid = [[1,7,3],[9,8,2],[4,5,6]]
    print("Expected Output: [[8,2,3],[9,6,7],[4,5,1]]")
    print("Actual Output: ", s.sortMatrix(grid))
