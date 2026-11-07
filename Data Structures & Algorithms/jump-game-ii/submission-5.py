class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums)]*len(nums)

        dp[-1] = 0

        for i in range(len(nums)-2,-1,-1):
            dp[i] = 1+min((dp[i+j] if i+j < len(nums) else len(nums) for j in range(1,nums[i]+1)), default=0)

        return dp[0]