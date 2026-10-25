import functools
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        [ # 1  2  3
            0, 0, 0, # 0
            0, 0, 0, # 1
            0, 0, 0, # 2
            0, 0, 0, # 3
            1, 1, 1, # 4
        ]
        
        dp = [[1 if i == amount else 0]*len(coins) for i in range(amount+1)]

        for r in range(len(dp)-2, -1, -1):
            for c in range(len(dp[r])-1, -1, -1):
                # Choose
                num_ways = 0
                if r + coins[c] <= amount:
                    num_ways += dp[r+coins[c]][c]

                if c + 1 < len(dp[0]):
                    num_ways += dp[r][c+1]

                dp[r][c] = num_ways

        return dp[0][0]

        # @functools.cache
        # def dfs(coin_i, curr_amount):
        #     if coin_i == len(coins):
        #         return 0
        #     elif curr_amount > amount:
        #         return 0
        #     elif curr_amount == amount:
        #         return 1

        #     # Choose or skip coin
        #     return dfs(coin_i, curr_amount+coins[coin_i])+dfs(coin_i+1, curr_amount)
