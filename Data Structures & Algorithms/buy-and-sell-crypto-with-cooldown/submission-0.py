class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        memo = {}
        def maxProfit(i, last_buy):
            if i >= len(prices): return 0

            if (i, last_buy) in memo: return memo[(i, last_buy)]
            if last_buy is not None:
                # sell now or later
                memo[(i, last_buy)] = max(
                    prices[i]-prices[last_buy]+maxProfit(i+2, None),
                    maxProfit(i+1, last_buy)
                )
                return memo[(i, last_buy)]

            # buy now or later.
            memo[(i, last_buy)] = max(
                maxProfit(i+1, i),
                maxProfit(i+1, None)
            )

            return memo[(i, last_buy)]

        return maxProfit(0, None)