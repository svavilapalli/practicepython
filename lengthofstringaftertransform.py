# You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:
# 
# Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".
# The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".
# Return the length of the resulting string after exactly t transformations.
# 
# Since the answer may be very large, return it modulo 109 + 7.

from typing import List
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 1_000_000_007
        dp = [0]*26
        prevs = []
        for c in s:
            dp[ord(c) - ord("a")]+=1
        for j in range(26):
            lst = []
            for p in range(1,26):
                prev = (j-p+26)%26
                if ((prev< j and prev+nums[prev] >= j) or (prev > j and (nums[prev] + prev) >= j+26)):
                    lst.append(prev)
            prevs.append(lst)
            
        for i in range(t):
            nxt = [0]*26
            for j in range(26):
                for prev in prevs[j]:
                    nxt[j]+=dp[prev]
            dp = nxt
        ans = sum(dp) % mod
        return ans


SL = Solution()
s = "abcyy"
t = 2
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
print("Expected  Output :  7")
print(f"Actual Output {SL.lengthAfterTransformations(s, t, nums)}")
