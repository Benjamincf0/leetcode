class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        tot_sum = sum(stones)
        max_sum = tot_sum//2

        dp = [[0]*(max_sum+1) for _ in range(len(stones))]

        for i in range(len(stones)):
            for max_sum in range(max_sum+1):
                dp[i][max_sum] = dp[i-1][max_sum] if i>0 else 0

                if stones[i] <= max_sum:
                    with_ith = stones[i] + (dp[i-1][max_sum-stones[i]] if i>0 else 0)
                    dp[i][max_sum] = max(dp[i][max_sum], with_ith)

        return tot_sum - 2*dp[-1][-1]