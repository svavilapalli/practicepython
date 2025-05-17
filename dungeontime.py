# There is a dungeon with n x m rooms arranged as a grid.
# 
# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.
# 
# Return the minimum time to reach the room (n - 1, m - 1).
# 
# Two rooms are adjacent if they share a common wall, either horizontally or vertically.
from typing import List
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
    
        pq = [(0, 0, 0, 1)]  # Start at (0,0) with time 0, next move costs 1
    
        visited = set()
    
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
        while pq:
            time, row, col, move_cost = heapq.heappop(pq)
            
            if row == n - 1 and col == m - 1:
                return time
            
            state = (row, col, move_cost)
            if state in visited:
                continue
            
            visited.add(state)
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if 0 <= new_row < n and 0 <= new_col < m:
                    new_time = max(time, moveTime[new_row][new_col])+move_cost
                    
                    new_move_cost = 3 - move_cost  
                    
                    heapq.heappush(pq, (new_time, new_row, new_col, new_move_cost))
        
        return -1  


s = Solution()
moveTime = [[0,4],[4,4]]
print("Expected output: 7")
print(f"Actual output {s.minTimeToReach(moveTime)}")
