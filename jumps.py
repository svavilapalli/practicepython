# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

# Example :
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

import heapq
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums)*2]*len(nums)
        dp[0] = 0
        for i,n in enumerate(nums):
            for j in range(1,n+1):
                if i+j<len(nums):
                    dp[i+j] = min(dp[i+j],dp[i]+1)
        return dp[-1]


nums = [2,3,1,1,4]
s= Solution()
print("Expected Output: 2")
print("Actual Output:",s.jump(nums))
