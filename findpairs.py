# You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:

# Add a positive integer to an element of a given index in the array nums2.
# Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 <= i < nums1.length and 0 <= j < nums2.length).
# Implement the FindSumPairs class:

# FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object with two integer arrays nums1 and nums2.
# void add(int index, int val) Adds val to nums2[index], i.e., apply nums2[index] += val.
# int count(int tot) Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.
 

# Example 1:

# Input
# ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
# [[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
# Output
# [null, 8, null, 2, 1, null, null, 11]

from collections import Counter
from typing import List
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.n1 = Counter(self.nums1)
        self.n2 = Counter(self.nums2)

    def add(self, index: int, val: int) -> None:
        if index <len(self.nums2):
            self.n2[self.nums2[index]] -=1
            self.nums2[index]+= val
            if self.nums2[index] in self.n2:
                self.n2[self.nums2[index]] +=1
            else:
                self.n2[self.nums2[index]] = 1

    def count(self, tot: int) -> int:
        cnt= 0
        for v in self.n1:
            if tot-v in self.n2:
                cnt += (self.n1[v]*self.n2[tot-v])
        return cnt


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

if __name__ == "__main__":
    ops = ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
    params = [[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
    result = []
    obj = None
    for op,param in zip(ops, params):
        print(op, param, obj)
        if op == "FindSumPairs":
            obj = FindSumPairs(param[0], param[1])
            result.append(None)
        elif op == "add" and obj:
            obj.add(param[0], param[1])
            result.append(None)
        elif op == "count" and obj:
            pairs = obj.count(param[0])
            result.append(pairs)
    
    print("Expected Output:  [None, 8, None, 2, 1, None, None, 11]")
    print("Actual Output: ",result)
        
