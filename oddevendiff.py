# You are given a string s and an integer k. Your task is to find the maximum difference between the frequency of two characters, freq[a] - freq[b], in a substring subs of s, such that:

# subs has a size of at least k.
# Character a has an odd frequency in subs.
# Character b has an even frequency in subs.
# Return the maximum difference.

# Note that subs can contain more than 2 distinct characters.

from collections import Counter
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        res = -n-1

        freq = dict(Counter(s[0:k]))

        def getedges(fq):
                
            cur_odd = -n
            cur_even = n+n
            for c in fq:
                if fq[c] != 0:
                    if fq[c]%2 == 0 and cur_even > fq[c]:
                        cur_even = fq[c]
                    elif fq[c] %2 ==1 and cur_odd < fq[c]:
                        cur_odd = fq[c]
            return cur_odd, cur_even

        cod, cev = getedges(freq)
        res = cod - cev

        for i in range(k,n+1):
            if i>k:
                if s[i-1] in freq:
                    freq[s[i-1]] += 1
                else:
                    freq[s[i-1]] = 1

            rf =freq.copy()
            cod, cev = getedges(rf)
            res = max(res,cod - cev)
            print(rf, res)
            st = 0
            while st+i <= n:
                if st > 0 :
                    nc = s[st+i-1]
                    oc = s[st-1]
                    print(st, oc, nc)
                    if oc != nc:
                        if rf[oc] >0:
                            rf[oc] -= 1
                        if nc not in freq:
                            rf[nc] = 1
                        else:
                            rf[nc] += 1
                        cod, cev = getedges(rf)
                        res = max(res, cod-cev)
                st +=1
        return res



if __name__ == "__main__":
    sl = Solution()
    s="1122211"
    k = 3
    print("Expected Output: 1")
    print("Actual Output: ",sl.maxDifference(s,k))
