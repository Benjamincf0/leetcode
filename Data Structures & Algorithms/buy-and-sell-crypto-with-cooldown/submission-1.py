class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Top down: O(n) Space: O(n)
        
        memo = {}
        def maxProfit(i, isSell):
            if i >= len(prices): return 0

            if (i, isSell) in memo: return memo[(i, isSell)]
            if isSell:
                # sell now or later
                memo[(i, isSell)] = max(
                    prices[i]+maxProfit(i+2, False),
                    maxProfit(i+1, isSell)
                )
                return memo[(i, isSell)]

            # buy now or later.
            memo[(i, isSell)] = max(
                maxProfit(i+1, True)-prices[i],
                maxProfit(i+1, False)
            )

            return memo[(i, isSell)]

        return maxProfit(0, None)