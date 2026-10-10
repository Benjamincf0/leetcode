class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, partial_sum):
            if i == len(nums):
                return 1 if partial_sum == target else 0

            if (i, partial_sum) in cache: return cache[(i, partial_sum)]
            withoutCur = dfs(i+1, partial_sum + nums[i])
            withCur = dfs(i+1, partial_sum - nums[i])
            res = withoutCur + withCur
            cache[(i, partial_sum)] = res
            return res

        return dfs(0, 0)

# 2 2 2
# ps = 0->2->4->6
#             ->2 *
#          ->0->2 *
#             ->0
#       ->-2->0->2 *
#              ->-2
#           ->-4 x