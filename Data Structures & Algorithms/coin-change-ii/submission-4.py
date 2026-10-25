class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Bottom-up DP Time O(n*m) & Space O(n*m)
        dp = [[1 if i == amount else 0]*len(coins) for i in range(amount+1)]

        for r in range(len(dp)-2, -1, -1):
            for c in range(len(dp[r])-1, -1, -1):
                # Choose
                if r + coins[c] <= amount:
                    dp[r][c] += dp[r+coins[c]][c]

                if c + 1 < len(dp[0]):
                    dp[r][c] += dp[r][c+1]

        return dp[0][0]