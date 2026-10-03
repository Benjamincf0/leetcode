from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)/2

        @cache
        def dfs(i, s):
            if s == tot: return True
            if i >= len(nums): return False

            return dfs(i+1, s) or dfs(i+1, s+nums[i])

        return dfs(0, 0)
