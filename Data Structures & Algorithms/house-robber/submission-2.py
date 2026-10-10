class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def maxProfit(i):
            if i >= len(nums): return 0
            if i in cache:
                return cache[i]
            ith_profit = nums[i]
            res = max(ith_profit + maxProfit(i+2),
                        maxProfit(i+1))
            cache[i] = res
            return res

        return maxProfit(0)