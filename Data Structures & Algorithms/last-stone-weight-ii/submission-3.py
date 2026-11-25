class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        tot_sum = sum(stones)
        max_sum = tot_sum//2

        memo = {}
        def maxWeight(i, max_sum):
            if i < 0: return 0
            if (i, max_sum) in memo: return memo[(i, max_sum)]

            without_ith = maxWeight(i-1, max_sum)
            if stones[i] > max_sum: return without_ith
            with_ith = stones[i]+maxWeight(i-1, max_sum-stones[i])

            memo[(i, max_sum)] = max(with_ith, without_ith)
            return memo[(i, max_sum)]

        return tot_sum - 2*maxWeight(len(stones)-1, max_sum)