from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dfs(curr_amount):
            if curr_amount > amount: return float("inf") 
            elif curr_amount == amount: return 1
            
            return 1 + min(dfs(curr_amount + i) for i in coins if i)

        res = dfs(0)
        return -1 if res == float("inf") else res-1