class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}
        def dfs(i, robbed_first):
            if i >= len(nums):
                return 0

            if (i, robbed_first) in memo: return memo[(i, robbed_first)]

            if i == len(nums)-1:
                memo[(i, robbed_first)] = 0 if robbed_first else nums[i]
                return memo[(i, robbed_first)]

            memo[(i, robbed_first)] = max(nums[i] + dfs(i+2, i == 0 or robbed_first),
                        dfs(i+1, robbed_first))

            return memo[(i, robbed_first)]

        return dfs(0, False)