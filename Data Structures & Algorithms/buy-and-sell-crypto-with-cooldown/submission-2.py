class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Top down: O(n) Space: O(n)
        dp_buy = [0]*(len(prices)+1)
        dp_sell = [0]*(len(prices)+1)

        dp_sell[-2] = prices[-1]

        for i in range(len(prices)-2,-1,-1):
            dp_buy[i] = max(dp_sell[i+1]-prices[i], dp_buy[i+1])
            dp_sell[i] = max(dp_sell[i+1], prices[i]+dp_buy[i+2])

        return dp_buy[0]