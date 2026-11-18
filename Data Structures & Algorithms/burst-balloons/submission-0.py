class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        memo = {}

        def dfs(l, r):
            if l > r: return 0
            if (l,r) in memo: return memo[(l,r)]

            memo[(l,r)] = max((nums[i]*(nums[l-1] if l>0 else 1)*(nums[r+1] if r<len(nums)-1 else 1)+
                dfs(l, i-1)+
                dfs(i+1,r) for i in range(l, r+1)))
            return memo[(l,r)]

        return dfs(0, len(nums)-1)