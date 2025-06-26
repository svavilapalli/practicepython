# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
#
# Example 1:
#
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
# [1,2,1],
# [2,1,1]]


from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dp = [[] for _ in range(len(nums))]
        dp[0] = [[n] for n in set(nums)]
        counts = [[] for _ in range(len(nums))]
        counts[0] = [{n:1} for n in set(nums)]
        totals = dict(Counter(nums))
        i = 1
        while i < len(nums):
            j =0
            for l in dp[i-1]:
                for n in set(nums):
                    if n not in counts[i-1][j] or counts[i-1][j][n]< totals[n]:
                        dp[i].append(l+[n])
                        counts[i].append(dict(Counter(dp[i][-1])))
                j+=1
            i+=1
        return dp[-1]


s = Solution()
nums = [1,1,2]
print("Expected Output: [[1,1,2], [1,2,1], [2,1,1]]")
print("Actual Output: ", s.permuteUnique(nums))
