class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # bottom-up dp Time O(n*m) ; Space O(m) ; n=len(nums) m=sum(nums)
        s = sum(nums)
        if abs(target) > abs(s): return 0
        prev = [0]*(2*s+1)
        prev[s] = 1
        cur = [0]*(2*s+1)

        for r in range(1, len(nums)+1):
            for c in range(2*s+1):
                n = nums[r-1]
                leftVal = c-n
                rightVal = c+n

                if 0<= leftVal < 2*s+1:
                    cur[c] += prev[leftVal]
                if 0<= rightVal < 2*s+1:
                    cur[c] += prev[rightVal]

            prev = cur
            cur = [0]*(2*s+1)

        return prev[s+target]