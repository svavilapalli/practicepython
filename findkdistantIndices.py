# You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.
# 
# Return a list of all k-distant indices sorted in increasing order.


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = set()
        i = 0
        while i<len(nums):
            if nums[i] == key:
                indices = range(max(0,i-k), min(len(nums),i+k+1))
                res= res.union(set(indices))
            i+=1
        return list(res)


s=  Solution()
nums = [3,4,9,1,3,9,5]
key = 9
k = 1
print("Expected Output: [1,2,3,4,5,6]")
print("Actual Output: ",s.findKDistantIndices(nums,key,k))
