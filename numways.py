# You are given a list of strings of the same length words and a string target.
# 
# Your task is to form target using the given words under the following rules:
# 
# target should be formed from left to right.
# To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
# Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
# Repeat the process until you form the string target.
# Notice that you can use multiple characters from the same string in words provided the conditions above are met.
#
# Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.
# 


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        wordcount = len(words)
        if wordcount == 0: 
            return 0
        wordlen = len(words[0])

        target_length = len(target)
        if target_length > wordlen:
            return 0
        poswords = ['']*wordlen
        for word in words:
            for i in range(wordlen):
                poswords[i] = poswords[i]+word[i]
        st = 0
        totalchances= 0
        notfound = False
        memo = {}
        def dfs(cpos, pos):
            origpos= pos
            if (cpos, pos) in memo:
                return memo[(cpos, pos)]
            ch = target[cpos]
            if cpos == target_length-1:
                val = sum([word.count(ch) for word in poswords[pos:]])
                memo[(cpos, pos)] = val 
                return val
            while pos < wordlen and ch not in poswords[pos]:
                pos += 1
            if pos >= wordlen:
                return 0
            chcount = poswords[pos].count(ch)
            nextcharcount = dfs(cpos+1, pos+1)
            charnextcount = dfs(cpos, pos+1)
            total = (chcount * nextcharcount + charnextcount)%  1_000_000_007
            memo[(cpos, origpos)] = total
            return (chcount * nextcharcount + charnextcount)%  1_000_000_007

        return dfs(0, 0) %  1_000_000_007



s= Solution()
words = ["acca","bbbb","caca"]
target = "aba"
print(s.numWays(words, target))
