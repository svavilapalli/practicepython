# You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.
# You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.
# Return the maximum sum of values that you can receive by attending events.

# Example:
# Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
# Output: 7
# Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.

from typing import List
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        def findevent(pos,newstart):
            
            l = pos
            r = len(events)-1
            if events[r][0]<newstart:
                return r+1
            while l<=r:
                mid = (l+r)//2
                if events[mid][0]==newstart:
                    while events[mid-1][0] == newstart:
                        mid-=1
                    return mid
                elif events[mid][0] < newstart:
                    l = mid+1
                else:
                    r = mid-1
            if events[mid][0]>=newstart:
                while events[mid-1][0]>=newstart and mid>=pos:
                    mid -= 1
                return mid
            else:
                return mid+1


        memo=  {}
        def attendevent(start,k):
            if (start,k) in memo:
                return memo[(start,k)]
            if (k==0):
                return 0
            elif start == len(events):
                return 0
            else:
                end = events[start][1]
                nextevent = findevent(start+1, end+1)
                memo[(start,k)]= max(events[start][2]+attendevent(nextevent,k-1), attendevent(start+1,k))
                return memo[(start,k)]

        return attendevent(0,k)
            

events = [[1,100,10],[18,92,87],[17,65,93],[40,63,40],[18,68,60],[42,73,21],[47,79,74],[5,98,57],[24,65,73],[28,86,42],[21,41,91],[93,95,17],[68,73,30],[41,78,3],[9,73,77],[47,92,96],[42,83,70],[76,77,2],[32,69,42],[43,80,54],[51,65,11],[21,71,96],[8,24,96],[24,82,77],[43,53,1],[33,66,46],[19,72,40],[20,81,53],[13,100,18],[29,84,98],[9,78,10],[2,43,99],[1,71,35],[14,23,86],[30,94,37],[6,26,98],[7,10,96],[7,20,61],[44,99,87],[28,72,56],[54,88,72],[42,70,6]]
k = 17
print("Expected Output: 304")
s = Solution()
print("Actual Output: ",s.maxValue(events,k))
