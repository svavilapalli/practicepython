# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example :

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
            elif res[-1][1] >= interval[0]:
                res[-1][1] = max(interval[1],res[-1][1])
            else:
                res.append(interval)
        return res


s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print("Expected Output: [[1,6],[8,10],[15,18]]")
print("Actual Output: ", s.merge(intervals))
