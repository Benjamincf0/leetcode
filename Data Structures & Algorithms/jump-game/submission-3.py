from functools import cache
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        @cache
        def dfs(i):
            if i == len(nums) -1 : return True
            if i >= len(nums): return False
            # print(i, nums[i], range(1, nums[i]+1))
            return any(dfs(i+j) for j in range(1, nums[i]+1))

        return dfs(0)