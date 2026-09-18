class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Top-down dp Time O(n^2) ; Space O(n^2)
        
        cache = {}
        def dfs(minimum, i):
            if i >= len(nums): return 0
            if (minimum, i) in cache: return cache[(minimum, i)]

            if minimum < nums[i]:
                res =  max(dfs(minimum, i+1), 1+dfs(nums[i], i+1))
                cache[(minimum, i)] = res
                return res
            else:
                res =  dfs(minimum, i+1)
                cache[(minimum, i)] = res
                return res

        return dfs(float("-inf"), 0)