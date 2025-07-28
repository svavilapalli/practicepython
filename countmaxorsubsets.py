# Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

# The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

 

# Example:

# Input: nums = [3,1]
# Output: 2
# Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
# - [3]
# - [3,1]

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        dp = [0] * (1 << 17)
        dp[0] = 1
        max_or = 0

        for num in nums:
            for i in range(max_or, -1, -1):
                dp[i | num] += dp[i]
            max_or |= num

        return dp[max_or]


if __name__ == "__main__":
    s = Solution()
    nums = [3,1]
    print("Expected Output: 2")
    print("Actual Output: ", s.countMaxOrSubsets(nums))
