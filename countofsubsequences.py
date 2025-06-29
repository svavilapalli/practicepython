# You are given an array of integers nums and an integer target.

# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 10^9 + 7

# Example:
# Input: nums = [2,3,3,4,6,7], target = 12
# Output: 61
# Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
# Number of valid subsequences (63 - 2 = 61).

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        l = len(nums)
        res= 0
        for i,n in enumerate(nums):
            if n*2>target:
                break
            end = target-n
            while l>i + 1 and nums[l-1]>end:
                l -= 1
            if res > 0:
                res+=1
            if  l == i+1:
                break
            length = l - i - 1
            cs= (2 ** length) -1
            res += cs
        if i> 0 and nums[0]*2<=target:
            res += 1
        return res % 1_000_000_007


s = Solution()
nums = [2,3,3,4,6,7]
target = 12
print("Expected Output: 61")
print("Actual Output : ",s.numSubseq(nums, target))
