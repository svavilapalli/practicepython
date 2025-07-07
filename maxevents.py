# You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
# You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.
# Return the maximum number of events you can attend.

# Example:
# Input: events = [[1,2],[2,3],[3,4]]
# Output: 3
# Explanation: You can attend all the three events.
# One way to attend them all is as shown.
# Attend the first event on day 1.
# Attend the second event on day 2.
# Attend the third event on day 3.
from typing import List
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        def search(nextDay, day):
            if nextDay[day] != day:
                nextDay[day] = search(nextDay, nextDay[day])
            return nextDay[day]
    
        events.sort(key =(lambda x:x[1]))
        nextDay = list(range(events[-1][1]+2))
        count = 0
        for start, end  in events:
            day = search(nextDay,start)
            if day <= end:
                count += 1
                nextDay[day] = search(nextDay, day+1)
        return count



events = [[1,2],[2,3],[3,4]]
print("Expected Output: 3")
s = Solution()
print("Actual Output: ", s.maxEvents(events))
