# Sherlock Holmes suspects his archenemy Professor Moriarty is once again plotting something diabolical. Sherlock's companion, Dr. Watson, suggests Moriarty may be responsible for MI6's recent issues with their supercomputer, The Beast.

# Shortly after resolving to investigate, Sherlock receives a note from Moriarty boasting about infecting The Beast with a virus. He also gives him a clue: an integer. Sherlock determines the key to removing the virus is to find the largest Decent Number having that number of digits.

# A Decent Number has the following properties:

# Its digits can only be 3's and/or 5's.
# The number of 3's it contains is divisible by 5.
# The number of 5's it contains is divisible by 3.
# It is the largest such number for its length.
# Moriarty's virus shows a clock counting down to The Beast's destruction, and time is running out fast. Your task is to help Sherlock find the key before The Beast is destroyed!

# For example, the numbers 55533333 and 555555 are both decent numbers because there are  3 5's and 5 3's in the first, and 6 5's in the second. They are the largest values for those length numbers that have proper divisibility of digit occurrences.

# Function Description

# Complete the decentNumber function in the editor below.

# decentNumber has the following parameter(s):

# int n: the length of the decent number to create
# Prints

# Print the decent number for the given length, or -1 if a decent number of that length cannot be formed. No return value is expected.

# Input Format

# The first line is an integer, t, the number of test cases.

# The next t lines each contain an integer n, the number of digits in the number to create.

# Sample Input

# STDIN   Function
# -----   --------
# 4       t = 4
# 1       n = 1 (first test case)
# 3       n = 3 (second test case)
# 5
# 11
# Sample Output

# -1
# 555
# 33333
# 55555533333
# Explanation

# For n=1, there is no Decent Number having 1 digit, so print -1.
# For n=3, 555 is the only possible number. (Decent Number Property 3).
# For n=5, 33333 is the only possible number. (Decent Number Property 2).
# For n=11, 55555533333 is the Decent Number. All other permutations of these digits are not decent (Decent Number Property 4).

# Language



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n, fptr):
    # Write your code here
    ans = ''
    if n%3==0:
        ans = '5'*n
    else:
        t = 0
        f = 0
        while n>0:
            n -= 5
            t += 5
            if n%3 ==0:
                f = n
                n==0
                break
        if n<0:
            ans = '-1'
        else:
            ans = '5'*f+'3'*t
    fptr.write(ans+"\n")

if __name__ == '__main__':
    t = int(input().strip())
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    for t_itr in range(t):
        
        n = int(input().strip())

        decentNumber(n, fptr)
    fptr.close()
