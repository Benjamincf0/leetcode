import functools
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @functools.cache
        def dfs(coin_i, curr_amount):
            if coin_i == len(coins):
                return 0
            elif curr_amount > amount:
                return 0
            elif curr_amount == amount:
                return 1

            return dfs(coin_i, curr_amount+coins[coin_i])+dfs(coin_i+1, curr_amount)

        return dfs(0, 0)