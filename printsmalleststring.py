# You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:
# 
# Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
# Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
# Return the lexicographically smallest string that can be written on the paper.

class Solution:
    def robotWithString(self, s: str) -> str:
        rs = s[::-1]
        t = ''
        res = ''
        for i in range(26):
            c = chr(i+ord('a'))
            if c in rs:
                res += c*rs.count(c)
                loc = rs.find(c)
                t = rs[loc+1:].replace(c,'') +t
                rs = rs[:loc]
                if rs == '':
                    return res + t
                while t != '' and min(rs) >= t[0]:
                    res += t[0]
                    t =t[1:]
        return res




sl = Solution()
s="mmuqezwmomeplrtskz"
print("Expected Output : eekstrlpmomwzqummz")
print("Actual Output : ",sl.robotWithString(s))
