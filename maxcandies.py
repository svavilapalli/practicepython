# You have n boxes labeled from 0 to n - 1. You are given four arrays: status, candies, keys, and containedBoxes where:
# 
# status[i] is 1 if the ith box is open and 0 if the ith box is closed,
# candies[i] is the number of candies in the ith box,
# keys[i] is a list of the labels of the boxes you can open after opening the ith box.
# containedBoxes[i] is a list of the boxes you found inside the ith box.
# You are given an integer array initialBoxes that contains the labels of the boxes you initially have. You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.
#
# Return the maximum number of candies you can get following the rules above.

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        collected = [False]*n
        availablekeys = set()
        boxesinhand = set()
        dq = deque(initialBoxes)
        tot_candies = 0
        while dq:
            box = dq.popleft()
            if box in availablekeys:
                status[box] = 1
            if status[box] == 1 and (not collected[box]):
                availablekeys=availablekeys.union(keys[box])
                tot_candies += candies[box]
                collected[box] = True
                for b in containedBoxes[box]:
                    dq.append(b)
                for b in availablekeys.intersection(boxesinhand):
                    if not collected[b]:
                        dq.append(b)
            elif not collected[box]:
                boxesinhand.add(box)

        return tot_candies



s = Solution()
status = [1,0,1,0]
candies = [7,5,4,100]
keys = [[],[],[1],[3]]
containedBoxes = [[1,2],[3],[],[]]
initialBoxes = [0]


print("Expected Output: 16")
print("Actual Output: ", s.maxCandies(status, candies, keys, containedBoxes, initialBoxes))
