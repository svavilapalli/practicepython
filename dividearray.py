# You are given an integer array nums of size n where n is a multiple of 3 and a positive integer k.
# 
# Divide the array nums into n / 3 arrays of size 3 satisfying the following condition:
# 
# The difference between any two elements in one array is less than or equal to k.
# Return a 2D array containing the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

from typing import List
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0,len(nums),3):
            if nums[i+2] - nums[i]>k:
                return []
            ans.append([nums[i], nums[i+1],nums[i+2]])
        return ans

# You are given an integer array nums and an integer k. You may partition nums into one or more subsequences such that each element in nums appears in exactly one of the subsequences.
# 
# Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in each subsequence is at most k.
# 
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 1
        curmin = nums[0]
        for c in nums:
            if c-curmin > k:
                curmin = c
                count+=1
        return count

s.Solution()
print("Expected Output: [[1,1,3],[3,4,5],[7,8,9]]")
print("Actual Output: ",s.divideArray([1,3,4,8,7,9,3,5,1], 2))
print("Expected Output: 2")
print("Actual Output: ",s.partitionArray([3,6,1,2,5], 2))
