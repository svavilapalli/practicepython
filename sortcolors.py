# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# 
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# 
# You must solve this problem without using the library's sort function.

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        begin = 0
        end = len(nums) - 1
        curr = 0
        while curr<=end:
            if nums[curr] == 0:
                nums[curr],nums[begin] = nums[begin],nums[curr]
                begin += 1
                curr +=1
            elif nums[curr] == 2:
                nums[curr],nums[end] = nums[end],nums[curr]
                end -= 1
            else:
                curr += 1


s = Solution()
nums = [2,0,2,1,1,0]
s.sortColors(nums)
print("Expected output [0, 0, 1, 1, 2, 2]")
print(f"Actual output {nums}")
