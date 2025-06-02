# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
#
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)
        mask = (1<<n+2)
        n_mask = (1<<n+2)
        for i in range(1,n+2):
            mask |= (1 << i)
            if i <= n:
                if 0< nums[i-1]<=n:
                    n_mask |= (1<<nums[i-1])
        mask = mask^n_mask
        for i in range(1,n+2):
            if mask &( 1<<i):
                return i
        return 1
