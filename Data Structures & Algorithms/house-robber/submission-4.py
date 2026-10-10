class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time O(n) ; Space O(1)
        
        # maxProfits = [0] * (len(nums)+2)
        maxProfitNextHouse = 0
        maxProfitNextNextHouse = 0

        for i in range(len(nums)-1, -1, -1):
            # maxProfit = max(max with this house, max without this house)
            maxWithThisHouse = nums[i] + maxProfitNextNextHouse
            maxWithoutThisHouse = maxProfitNextHouse
            maxProfit = max(maxWithThisHouse, maxWithoutThisHouse)
            # maxProfits[i] = maxProfit
            maxProfitNextNextHouse = maxProfitNextHouse
            maxProfitNextHouse = maxProfit

        return maxProfitNextHouse