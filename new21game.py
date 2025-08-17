# Alice plays the following game, loosely based on the card game "21".
# Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.
# Alice stops drawing numbers when she gets k or more points.
# Return the probability that Alice has n or fewer points.
# Answers within 10-5 of the actual answer are considered accepted.

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        dp = [0.0] * maxPts
        dp[0] = 1.0

        window_sum = 1.0
        result = 0.0

        for i in range(1, n + 1):
            prob = window_sum / maxPts

            if i < k:
                window_sum += prob
            else:
                result += prob

            if i >= maxPts:
                window_sum -= dp[i % maxPts]

            dp[i % maxPts] = prob

        return result


if __name__ == "__main__":
    n = 21
    k = 17
    maxPts = 10
    print("Expected Output: 0.73278")
    s = Solution()
    print("Actual Output:", s.new21Game(n, k, maxPts))
