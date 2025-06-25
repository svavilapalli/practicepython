# Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k, return the kth (1-based) smallest product of nums1[i] * nums2[j] where 0 <= i < nums1.length and 0 <= j < nums2.length.
# 
#
# Example 1:
#
# Input: nums1 = [2,5], nums2 = [3,4], k = 2
# Output: 8
# Explanation: The 2 smallest products are:
# - nums1[0] * nums2[0] = 2 * 3 = 6
# - nums1[0] * nums2[1] = 2 * 4 = 8
# The 2nd smallest product is 8.

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        li = len(nums1)
        lj = len(nums2)

        def cntLessEq(A, B, a, b, x):
            cnt=0
            j = b-1
            for i in range(a):
                while j>=0 and A[i]*B[j]>x:
                    j -= 1
                cnt+=j+1            
            return cnt

        a0 = li
        for i in range(len(nums1)):
            if nums1[i]>=0:
                a0 = i
                break
        b0 = lj
        for i in range(len(nums2)):
            if nums2[i]>=0:
                b0 = i
                break
        
        A0 = nums1[:a0] #    // <0
        A1 = nums1[a0:]      #// >=0
        B0 = nums2[:b0]    #// <0
        B1 = nums2[b0:]      #// >=0

        a1 = li-a0
        b1 = lj-b0
        cntNeg = a0*b1+a1*b0
        if k<=cntNeg:
            # // need to reverse A1, B1, but keep the negative A0, B0
            A1 = A1[::-1]
            B1 = B1[::-1]
            l=-10000000000
            r=0
            # m, ans;
            while (l<=r):
                m=(l+r)//2
                cnt=cntLessEq(A0, B1, a0, b1, m)+cntLessEq(A1, B0, a1, b0, m)
                if (cnt<k):
                    l=m+1
                else:
                    ans=m
                    r=m-1
            return ans
        else:
            # // need to reverse A0, B0, but keep the non-negative A1, B1
            k-=cntNeg
            A0 = A0[::-1]
            B0 = B0[::-1]
            l=0
            r=10000000000
            #  m, ans;
            while (l<=r):
                m=(l+r)//2
                cnt=cntLessEq(A1, B1, a1, b1, m)+cntLessEq(A0, B0, a0, b0, m)
                # print(cnt)
                if (cnt<k):
                    l=m+1
                else:
                    ans=m
                    r=m-1
            return ans



nums1 = [2,5]
nums2 = [3,4]
k = 2
sl = Solution()
print("Expected Output:  8")
print("Actual Output: ",sl.kthSmallestProduct(nums1, nums2,k))
