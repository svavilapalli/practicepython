# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
# Return the largest lucky integer in the array. If there is no lucky integer return -1.

# Example:

# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = dict(Counter(arr))
        counts = sorted(counts.items(), reverse = True)
        for key,count in counts:
            if key == count:
                return key
        return -1


s= Solution()
arr = [2,2,3,4]
print("Expected Output: 2")
print("Actual Output: ", s.findLucky(arr))
