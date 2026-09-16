class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        

        def dfs(i):
            if i in memo: return memo[i]
            if i == len(nums) -1 : return True
            if i >= len(nums): return False
            # print(i, nums[i], range(1, nums[i]+1))
            memo[i] = any(dfs(i+j) for j in range(1, nums[i]+1))
            return memo[i]

        return dfs(0)