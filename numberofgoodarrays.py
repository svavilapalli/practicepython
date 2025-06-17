# You are given three integers n, m, k. A good array arr of size n is defined as follows:

# Each element in arr is in the inclusive range [1, m].
# Exactly k indices i (where 1 <= i < n) satisfy the condition arr[i - 1] == arr[i].
# Return the number of good arrays that can be formed.

# Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: n = 3, m = 2, k = 1

# Output: 4

# Explanation:

# There are 4 good arrays. They are [1, 1, 2], [1, 2, 2], [2, 1, 1] and [2, 2, 1].
# Hence, the answer is 4.
# Example 2:

# Input: n = 4, m = 2, k = 2

# Output: 6

# Explanation:

# The good arrays are [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2], [2, 1, 1, 1], [2, 2, 1, 1] and [2, 2, 2, 1].
# Hence, the answer is 6.
# Example 3:

# Input: n = 5, m = 2, k = 0

# Output: 2

# Explanation:

# The good arrays are [1, 2, 1, 2, 1] and [2, 1, 2, 1, 2]. Hence, the answer is 2.


import math
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        fact= k_fact= n_k_fact= n_fact = 1
        ans = 0
        if k == 0:
            ans = (m* (m-1) ** (n-1))%1_000_000_007
        elif k==n-1:
            return m
        else:
            num = min(k, n-1-k)
            # for i in range(1,num+1):
            #     fact = i*fact
            #     n_fact = n_fact * (n-i)
            # p = n_fact//fact
            p = math.comb(n-1, k)
            ans = ((m-1)**(n-k-1)*m*p)%1_000_000_007
        return ans




s = Solution()
n,m, k =3,2,1
print("Expected Output: 4")
print("Actual Output: ")
print(s.countGoodArrays(n,m,k))
