class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l=0
        r=1

        while r < len(prices):
            leftPrice = prices[l]
            rightPrice = prices[r]
            profit=rightPrice-leftPrice

            if profit < 0:
                l=r
                r+=1
            else:
                maxProfit = max(maxProfit, profit)
                r+=1
        return maxProfit