# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        n = len(nums)
        res = set()
        nums.sort()
        r_l = l=0
        r_h = h = n-1
        pivot1 = h
        pivot2 = l
        r_h -=1
        res = set()
        if sum(nums[-4:]) < target or sum(nums[:4])> target:
            return [] 
        while pivot1 > 2:
            pivot2 = l
            while pivot1 > pivot2+2:
                h_val = nums[pivot1]
                l_val = nums[pivot2]
                r_l = pivot2+1
                r_h = pivot1-1
                while r_l < r_h:
                    sumval = nums[r_l] + nums[r_h] +h_val+l_val
                    if sumval == target:
                        res.add((l_val,nums[r_l], nums[r_h],h_val))
                        r_l+=1
                        r_h-=1
                    elif sumval > target:
                        r_h-=1
                    else:
                        r_l+=1
                pivot2 += 1
            pivot1-=1
        return [[a,b,c,d] for a,b,c,d in res]


s= Solution()
nums = [0,0,0,0]
target = 0
print("Expected Output: [[0, 0, 0, 0]]")
print("Actual Output: ",s.fourSum(nums, target))
nums = [1,0,-1,0,-2,2]
target = 0
print("Expected Output: [[-2, -1, 1, 2], [-1, 0, 0, 1], [-2, 0, 0, 2]]")
print("Actual Output: ",s.fourSum(nums, target))
