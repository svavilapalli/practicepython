# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        results={}
        def multiply_single(d, value):
            if d in results:
                return results[d]
            carry = 0
            cm = []
            dm = int(d)
            for n in value:
                cv = int(n)
                pr = cv*dm
                cm.append(str((pr+carry)%10))
                carry = (pr+carry)//10
            if carry>0:
                cm.append(str(carry))
            results[d] = ''.join(cm)
            return results[d]
        m , v = len(num1), len(num2)
        if m < v:
            mul, val = num1[::-1], num2[::-1]
        else:
            mul, val = num2[::-1], num1[::-1]
            m, v = v, m
        digits=[]
        for i in range(m):
            s = '0'*i+multiply_single(mul[i], val)
            digits.append(int(s[::-1]))
        
        return str(sum(digits))


s= Solution()
num1 = "123"
num2 = "456"
print("Expected Output: \"56088\"")
print("Actual Output: ", s.multiply(num1, num2))
