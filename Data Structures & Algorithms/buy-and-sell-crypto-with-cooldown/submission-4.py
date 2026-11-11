class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Bottom down: O(n) Space: O(1)
        cur_buy = 0
        next_buy = 0
        nextnext_buy = 0

        cur_sell = prices[-1]
        next_sell = 0

        for i in range(len(prices)-2,-1,-1):
            next_sell = cur_sell
            nextnext_buy, next_buy = next_buy, cur_buy

            cur_buy = max(next_sell-prices[i], next_buy)
            cur_sell = max(next_sell, prices[i]+nextnext_buy)

        return cur_buy