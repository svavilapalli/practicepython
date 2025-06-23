# A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.

# For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.
# On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.
# Given the base k and the number n, return the sum of the n smallest k-mirror numbers.


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        
        def getdecimal(num, base):
            res = 0
            mul = 1
            while num>0:
                res = res + (num%10)*mul
                mul = mul *base
                num = num//10
            return res


        def getnextnum(num, base):
            if  num <base-1:
                return num +1
            if num == base-1:
                return 11
            s = str(num)
            l = len(s)
            h = l//2
            if l%2 == 0:
                half = s[:h]
            else:
                half = s[:h+1]
            nxt = ['']*(len(half)+1)
            i = -1
            while i>= -(len(half)):
                if int(half[i]) == base-1:
                    nxt[i]= '0'
                    i-=1
                else:
                    nxt[i] = str(int(half[i])+1)
                    i-=1
                    break
            while i>=-(len(half)):
                nxt[i] = half[i]
                i-=1
            if nxt[1] == '0':
                nxt[0] = '1'
                suffix = (nxt[:h])[::-1]
            else:
                suffix = (nxt[1:h+1])[::-1]
            return int(''.join( nxt+suffix))


        total = count = 0
        num = 1
        while count < n:
            decnum = getdecimal(num, k)
            snum = str(decnum)
            if snum == snum[::-1]:
                count += 1 
                total += decnum
            num = getnextnum(num, k)

        return total


s= Solution()
print("Expected Output : 20379000")
res= s.kMirror(7, 17)
ptint("Actual Output: ", res)
