# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.

# Example:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        added = False
        n = len(intervals)
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                
                if not added:
                    res.append(newInterval)
                    added = True
                res += intervals[i:]
                break
            elif not added:
                newInterval[0] = min(interval[0],newInterval[0])
                newInterval[1] = max(interval[1],newInterval[1])
                res.append(newInterval)
                added = True
            elif added:
                if res[-1][1] < interval[0]:
                    res += intervals[i:]
                    break
                else:
                    res[-1][1] = max(res[-1][1],interval[1])
            else:
                res += intervals[i:]
                break
        if not added:
            res.append(newInterval)
        return res


s = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print("Expected Output: [[1,5],[6,9]]")
print("Actual Output: ",s.insert(intervals, newInterval))
