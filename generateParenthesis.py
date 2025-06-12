# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# 
# Input: n = 1
# Output: ["()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def getParanthesis(val):
            if val == 0:
                return set()
            if val == 1:
                return {"()"}
            else:
                sub = getParanthesis(val-1)
                res = set()
                for pat in sub:
                    res.add("("+pat+")")
                    l = len(pat)
                    for i in range(l):
                        c = pat[i]
                        if c =='(':
                            openc = 1
                            j = i+1
                            while j <l:
                                if pat[j] == '(':
                                    openc += 1
                                elif pat[j] == ')':
                                    openc -= 1
                                if openc == 0 and j+1<l:
                                    res.add(pat[:i]+"("+pat[i:j+1]+')'+pat[j+1:])
                                j += 1
                    res.add("()"+pat)
                    res.add(pat+"()")
                return  res 
        
        return list(getParanthesis(n))


s= Solution()
print("""Expected Output: ["((()))","(()())","(())()","()(())","()()()"]""")
print("""Actual Output: ",s.generateParenthesis(3))
