class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l=0
        r=1

        while r < len(prices):
            leftPrice = prices[l]
            rightPrice = prices[r]
            profit=rightPrice-leftPrice
            maxProfit = max(maxProfit, profit)

            if leftPrice > rightPrice:
                l=r
                r+=1
            else:
                r+=1
        return maxProfit