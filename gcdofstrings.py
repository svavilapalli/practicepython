# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# 
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        if (l1<l2 and str2.find(str1)==-1) or \
           (l1>=l2 and str1.find(str2)==-1):
           return ""
        if set(str2) != set(str1):
            return ""
        if l1<l2:
            if l2%l1 == 0:
                if str2 == str1*(l2//l1):
                    return str1
                else:
                    return ""
            base = str2[l1:]
        else:
            if l1%l2 == 0:
                if str1 == str2*(l1//l2):
                    return str2
                else:
                    return ""
            base = str1[l2:]
        actualb = baselen = len(base)
        f = 2
        while l1%baselen != 0 and l2%baselen !=0:
            while actualb%f != 0 and f<actualb:
                f+=1
            baselen = actualb//f
            f+=1
        if base != base[:baselen] *( actualb//baselen):
            return ""
        elif base[:baselen] *( l1//baselen) != str1:
            return ""
        elif base[:baselen] *( l2//baselen) != str2:
            return ""
        return base[:baselen] 
