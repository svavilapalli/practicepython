# You are given a string s and an array of strings words. All the strings of words are of the same length.
#
# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.
# 
# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        N = len(s)
        wordCount = len(words)
        wordSize = len(words[0])
        originalCount = dict(Counter(words))
        ans = []
        for offset in range(wordSize):
            currentCount = {}
            start = offset
            count = 0
            end = offset
            while end+wordSize <= N:
                currWord = s[end:end+wordSize]
                if currWord in originalCount:
                    if currWord in currentCount:
                        currentCount[currWord] += 1
                    else:
                        currentCount[currWord] = 1
                    count += 1
                    while currentCount[currWord] > originalCount[currWord]:
                        startWord = s[start:start+wordSize]
                        currentCount[startWord] -= 1
                        start += wordSize
                        count -= 1
                    if count == wordCount:
                        ans.append(start)
                else:
                    count = 0
                    start = end+wordSize
                    currentCount.clear()
                end += wordSize
        return ans
