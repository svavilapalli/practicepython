# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MINX, MAXX = -2**31, 2**31-1  
        inc = ans = 1
        neg= False
        if divisor>0> dividend or dividend >0 >divisor:
            neg = True
        if dividend == 0:
            return 0
        top = abs(dividend)
        dinc = rb = bot = abs(divisor)
        if bot == 1:
            return min(top,MAXX) if not neg else max(-top, MINX)
        if top < bot:
            return 0
        while top >= rb+bot:
            if rb+dinc <= top:
                rb += dinc
                ans += inc
                inc += inc
                dinc += dinc
            else:
                inc = 1
                dinc = bot
            if neg and -ans < MINX:
                return MINX
            elif ans > MAXX:
                return MAXX
        return ans if not neg else -ans


s = Solution()
print(s.divide(10,3))
