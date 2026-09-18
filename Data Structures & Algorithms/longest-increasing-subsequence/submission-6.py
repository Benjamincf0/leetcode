class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Top-down dp Time O(n^2) ; Space O(n^2)
        if len(nums) == 1: return 1
        
        # len of  max subsequence starting at i
        dp = [1]*len(nums)
        ml = 0

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
                ml = max(dp[i], ml)

        return ml