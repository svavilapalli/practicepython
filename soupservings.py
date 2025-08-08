# You have two soups, A and B, each starting with n mL. On every turn, one of the following four serving operations is chosen at random, each with probability 0.25 independent of all previous turns:

# pour 100 mL from type A and 0 mL from type B
# pour 75 mL from type A and 25 mL from type B
# pour 50 mL from type A and 50 mL from type B
# pour 25 mL from type A and 75 mL from type B
# Note:

# There is no operation that pours 0 mL from A and 100 mL from B.
# The amounts from A and B are poured simultaneously during the turn.
# If an operation asks you to pour more than you have left of a soup, pour all that remains of that soup.
# The process stops immediately after any turn in which one of the soups is used up.

# Return the probability that A is used up before B, plus half the probability that both soups are used up in the same turn. Answers within 10-5 of the actual answer will be accepted.

 

# Example:

# Input: n = 50
# Output: 0.62500
# Explanation: 
# If we perform either of the first two serving operations, soup A will become empty first.
# If we perform the third operation, A and B will become empty at the same time.
# If we perform the fourth operation, B will become empty first.
# So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.


from math import ceil

dp = [[-1] * 201 for _ in range(201)]

class Solution:

    def dfs( self , A , B ) :
        A = int(A)
        B = int(B)
        if A <= 0 and B > 0 :
            return 1.0
        if A <= 0 and B <= 0 :
            return 0.5
        if A > 0 and B <= 0 :
            return 0.0
        if dp[A][B] != -1 :
            return dp[A][B]
        ans = 0.25 * (
            self.dfs( A - 4 , B ) +
            self.dfs( A - 3 , B - 1 ) +
            self.dfs( A - 2 , B - 2 ) +
            self.dfs( A - 1 , B - 3 )
        )
        dp[A][B] = ans
        return ans

    def soupServings(self, n: int) -> float:
        if n > 5000 :
            return 1.0
        for i in range(201) :
            for j in range(201) :
                dp[i][j] = -1
        N = int( ceil( n / 25.0 ) )
        return self.dfs( N , N )

if __name__ == "__main__":
    n = 50
    print("Expected Output: 0.62500")
    s = Solution()
    print("Actual Output: ", s.soupServings(n))
