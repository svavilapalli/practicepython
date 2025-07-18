# You are given a 0-indexed integer array nums consisting of 3 * n elements.

# You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:

# The first n elements belonging to the first part and their sum is sumfirst.
# The next n elements belonging to the second part and their sum is sumsecond.
# The difference in sums of the two parts is denoted as sumfirst - sumsecond.

# For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
# Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
# Return the minimum difference possible between the sums of the two parts after the removal of n elements.

 
# Example:

# Input: nums = [7,9,5,8,1,3]
# Output: 1
# Explanation: Here n = 2. So we must remove 2 elements and divide the remaining array into two parts containing two elements each.
# If we remove nums[2] = 5 and nums[3] = 8, the resultant array will be [7,9,1,3]. The difference in sums will be (7+9) - (1+3) = 12.
# To obtain the minimum difference, we should remove nums[1] = 9 and nums[4] = 1. The resultant array becomes [7,5,8,3]. The difference in sums of the two parts is (7+5) - (8+3) = 1.
# It can be shown that it is not possible to obtain a difference smaller than 1.



from typing import List
import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        m = n // 3
        
        # Arrays to store the minimum sum of first m elements up to each position
        # and maximum sum of last m elements from each position
        min_sum_left = [0] * n
        max_sum_right = [0] * n
        
        # For the left part: maintain minimum sum of m elements
        # Use a max heap to keep track of the m smallest elements
        left_heap = []
        current_sum = 0
        
        # Initialize with first m elements
        for i in range(m):
            heapq.heappush(left_heap, -nums[i])  # Use negative for max heap
            current_sum += nums[i]
        
        min_sum_left[m-1] = current_sum
        
        # Process remaining elements for left part
        for i in range(m, 2*m):
            # If current element is smaller than the largest in our m elements
            if nums[i] < -left_heap[0]:
                # Remove the largest element
                removed = -heapq.heappop(left_heap)
                current_sum -= removed
                # Add the current element
                heapq.heappush(left_heap, -nums[i])
                current_sum += nums[i]
            
            min_sum_left[i] = current_sum
        
        # For the right part: maintain maximum sum of m elements
        # Use a min heap to keep track of the m largest elements
        right_heap = []
        current_sum = 0
        
        # Initialize with last m elements
        for i in range(n-m, n):
            heapq.heappush(right_heap, nums[i])  # Min heap
            current_sum += nums[i]
        
        max_sum_right[n-m] = current_sum
        
        # Process remaining elements for right part (going backwards)
        for i in range(n-m-1, m-1, -1):
            # If current element is larger than the smallest in our m elements
            if nums[i] > right_heap[0]:
                # Remove the smallest element
                removed = heapq.heappop(right_heap)
                current_sum -= removed
                # Add the current element
                heapq.heappush(right_heap, nums[i])
                current_sum += nums[i]
            
            max_sum_right[i] = current_sum
        
        # Find minimum difference
        min_diff = float('inf')
        for i in range(m-1, 2*m):
            left_sum = min_sum_left[i]
            right_sum = max_sum_right[i+1]
            min_diff = min(min_diff, left_sum - right_sum)
        
        return min_diff


if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    nums1 = [7,9,5,8,1,3]
    print("Expected Output: 6")
    print(f"Actual Output: {sol.minimumDifference(nums1)}")
    
    
