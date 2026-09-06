class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Time O(n) ; Space O(n)
        cost = [0] + cost
        dp = [None] * len(cost)
        dp[0], dp[1] = cost[0], cost[0]+cost[1]

        for i in range(2, len(dp)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])