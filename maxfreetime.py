# You are given an integer eventTime denoting the duration of an event, where the event occurs from time t = 0 to time t = eventTime.

# You are also given two integer arrays startTime and endTime, each of length n. These represent the start and end time of n non-overlapping meetings, where the ith meeting occurs during the time [startTime[i], endTime[i]].

# You can reschedule at most k meetings by moving their start time while maintaining the same duration, to maximize the longest continuous period of free time during the event.

# The relative order of all the meetings should stay the same and they should remain non-overlapping.

# Return the maximum amount of free time possible after rearranging the meetings.

# Note that the meetings can not be rescheduled to a time outside the event.

 
# Example:

# Input: eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]

# Output: 6

# Explanation:
# Reschedule the meeting at [2, 4] to [1, 3], leaving no meetings during the time [3, 9].

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gaps= [0]*(k+1)
        pos =prev =cursum= 0
        res= 0
        notfull = True
        for i in range(len(startTime)):
            if notfull:
                gaps[pos] = startTime[i]- prev
                cursum += gaps[pos]
            else:
                cursum -= gaps[0]
                del gaps[0]
                gaps.append(startTime[i]- prev)
                cursum += gaps[-1]
            prev = endTime[i]
            if pos < k:
                pos+=1
            else:
                notfull = False
            res = max(res, cursum)

        if not notfull:
            cursum -= gaps[0]
        cursum = cursum + (eventTime-endTime[-1])
        res = max(res, cursum)
        return res


def maxFreeTime_faster(self, t: int, k: int, s: List[int], e: List[int]) -> int:
        q = [*map(sub,s+[t],[0]+e)]
        return max(accumulate(map(sub,q[k+1:],q),lambda p,w:p+w,initial=sum(q[:k+1])))
        return max(accumulate(zip(q[k+1:],q),lambda p,w:p+w[0]-w[1],initial=sum(q[:k+1])))
        return max(accumulate(range(k+1,len(q)),lambda p,i:p+q[i]-q[i-k-1],initial=sum(q[:k+1])))


s= Solution()
eventTime = 10
k = 1
startTime = [0,2,9]
endTime = [1,4,10]
print("Expected Output: 6")
print("Actual Output: ", s.maxFreeTime(eventTime, k, startTime, endTime))
