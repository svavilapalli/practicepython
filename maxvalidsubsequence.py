
# You are given an integer array nums.
# A subsequence sub of nums with length x is called valid if it satisfies:

# (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
# Return the length of the longest valid subsequence of nums.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

# Example:

# Input: nums = [1,2,3,4]

# Output: 4


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        maxlength = 0
        n = len(nums)
        if n<=2:
            return n
        ee = eo = oe = oo = 0
        for v in nums:
            if v%2 == 0:
                ee+=1
                eo=1+oe
            else:
                oo+=1
                oe = 1+eo

        return max(ee, oe, eo, oo)



if __name__ == "__main__":
    nums = [1,2,1,1,2,1,2]
    s= Solution()
    print("Expected Output: 6")
    print("Actual Output: ",s.maximumLength(nums))
