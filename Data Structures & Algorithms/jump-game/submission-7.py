class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        
        def dfs_wrapper(k):
            if k in memo: return memo[k]

            def dfs(i):
                if i == len(nums) -1 : return True
                if i >= len(nums): return False
                # print(i, nums[i], range(1, nums[i]+1))
                return any(dfs_wrapper(i+j) for j in range(1, nums[i]+1))

            r = dfs(k)
            memo[k] = r
            return r

        return dfs_wrapper(0)