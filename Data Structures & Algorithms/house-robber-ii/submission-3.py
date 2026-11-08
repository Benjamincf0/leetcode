class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        dp = [[0,0] for _ in range(len(nums)+1)]
        # if we didn't rob the first house, we can rob the last.
        dp[-2][0] = nums[-1]
        # print(dp)

        for i in range(len(dp)-3,-1,-1):
            dp[i][0] = max(dp[i+1][0], nums[i]+dp[i+2][0])
            dp[i][1] = max(dp[i+1][1], nums[i]+dp[i+2][1])

        # print(dp)

        return max(dp[0][1],dp[1][0])