# Given a positive integer n, there exists a 0-indexed array called powers, composed of the minimum number of powers of 2 that sum to n. The array is sorted in non-decreasing order, and there is only one way to form the array.
# You are also given a 0-indexed 2D integer array queries, where queries[i] = [lefti, righti]. Each queries[i] represents a query where you have to find the product of all powers[j] with lefti <= j <= righti.

# Return an array answers, equal in length to queries, where answers[i] is the answer to the ith query. Since the answer to the ith query may be too large, each answers[i] should be returned modulo 109 + 7.

# Example:

# Input: n = 15, queries = [[0,1],[2,2],[0,3]]
# Output: [2,4,64]
# Explanation:
# For n = 15, powers = [1,2,4,8]. It can be shown that powers cannot be a smaller size.
# Answer to 1st query: powers[0] * powers[1] = 1 * 2 = 2.
# Answer to 2nd query: powers[2] = 4.
# Answer to 3rd query: powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64.
# Each answer modulo 109 + 7 yields the same answer, so [2,4,64] is returned.

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        b = bin(n)
        bits = (b[2:])[::-1]
        powers = []
        i = 0
        for bit in bits:
            if bit == '1':
                powers.append(2**i)
            i+=1
        MOD = 1_000_000_007
        # print(powers)
        answers = []
        for s,e in queries:
            ans = 1
            for p in powers[s:e+1]:
                ans= (ans * p)%MOD
            answers.append(ans)
        return answers

if __name__ == "__main__":
    n = 15
    queries = [[0,1],[2,2],[0,3]]
    print("Expect Output: [2,4,64]")
    s = Solution()
    print("Actual Output: ",s.productQueries(n, queries))
