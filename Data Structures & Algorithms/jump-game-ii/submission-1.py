class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def minJumps(i): 
            if i >= len(nums):
                return float("inf")
            elif i == len(nums)-1:
                return 0

            if i in memo: return memo[i]
            memo[i] = 1 + min(list(minJumps(i+j) for j in range(1,nums[i]+1)), default=0)
            return memo[i]

        return minJumps(0)