# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

# Return the maximum score you can get by erasing exactly one subarray.

# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 

# Example:

# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int: 
        score = 0
        visited = {}
        curstart = 0
        curscore = 0
        for i,n in enumerate(nums):
            if n in visited:
                for j in range(curstart,visited[n]):
                    curscore -= nums[j]
                    visited.pop(nums[j])
                curstart = visited[n]+1
                visited[n]=i
            else:
                visited[n]=i
                curscore += n
            score = max(score, curscore)
        return score


if __name__ == "__main__":
    s = Solution()
    nums = [4,2,4,5,6]
    print("Expected Output: 17")
    print("Actual Output: ",s.maximumUniqueSubarray(nums))
