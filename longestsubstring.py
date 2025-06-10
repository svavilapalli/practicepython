# Given a string s, find the length of the longest substring without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        charset= set()
        curlen = 0
        maxlen = 0
        for i in range(len(s)):
            c= s[i]
            if c not in charset:
                charset.add(c)
                curlen += 1
                if maxlen <curlen:
                    maxlen = curlen
            else:
                old = s.find(c,start)
                for j in range(start, old):
                    charset.remove(s[j])
                start = old+1
                curlen = i-start+1
            print(start, i, curlen, c, charset)
        return maxlen


if __name__ =="__main__":
    sl =Solution()
    s = "abcabcbb"
    print("Expected output : 3")
    print("Actual Output: ",sl.lengthOfLongestSubstring(s))
