# Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.
# You are given a string word, which represents the final output displayed on Alice's screen. You are also given a positive integer k.
# Return the total number of possible original strings that Alice might have intended to type, if she was trying to type a string of size at least k.
# Since the answer may be very large, return it modulo 109 + 7.

 

# Example :
# Input: word = "aabbccdd", k = 7
# Output: 5
# Explanation:
# The possible strings are: "aabbccdd", "aabbccd", "aabbcdd", "aabccdd", and "abbccdd".

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod= 1_000_000_007
        n = len(word)
        if n <k:
            return 0
        if n == k:
            return 1

        seg = [1]
        ccount = 1
        rep = ''
        for i in range(1,len(word)):
            if word[i]== word[i-1]:
                seg[-1]+=1
                rep += word[i]
            else:
                seg.append(1)
        m = len(seg)
        if max(seg) == 1:
            return 1
        total = 1
        takeMod = False
        for x in seg:
            total*=x
            if total>=mod:
                total%=mod
                takeMod=True
        if k<=m:
            return total
        maxT=k-m
        dp=[[0]*2000]*2
        prefix=[0]*2001
        dp[0][0]=1

        for j in range(m):
            s=seg[j]
            for i in range(maxT):
                prefix[i+1]=(prefix[i]+dp[j&1][i])%mod 
                L=max(0, i-(s-1))
                R=i
                dp[(j+1)&1][i]=(prefix[R+1]-prefix[L]+mod)%mod
            
        lessK=0
        for x in dp[m&1]:
            lessK=(lessK+x)%mod

        return (total-lessK+mod) % mod


s = Solution()
word = "aabbccdd"
k = 7
print("Expected Output: 5")
print("Actual Output", s.possibleStringCount(word, k))
