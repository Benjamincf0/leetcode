class Solution:
    def rob(self, nums: List[int]) -> int:
        maxProfits = [0] * (len(nums)+2)

        for i in range(len(nums)-1, -1, -1):
            # maxProfit = max(max with this house, max without this house)
            maxWithThisHouse = nums[i] + maxProfits[i+2]
            maxWithoutThisHouse = maxProfits[i+1]
            maxProfit = max(maxWithThisHouse, maxWithoutThisHouse)
            maxProfits[i] = maxProfit

        return maxProfits[0]