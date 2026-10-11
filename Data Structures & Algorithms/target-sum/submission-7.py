class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if target > s: return 0
        dp = [[0]*(2*s+1) for _ in range(len(nums)+1)]
        dp[0][s] = 1

        for r in range(1, len(nums)+1):
            for c in range(2*s+1):
                n = nums[r-1]
                leftVal = c-n
                rightVal = c+n

                if 0<= leftVal < 2*s+1:
                    dp[r][c] += dp[r-1][leftVal]
                if 0<= rightVal < 2*s+1:
                    dp[r][c] += dp[r-1][rightVal]

        # for r in dp:
        #     print(r)

        return dp[-1][s+target]
# 2 2 2    t = 2
# 0 0 0
# 0 0 0
# 0 0 0