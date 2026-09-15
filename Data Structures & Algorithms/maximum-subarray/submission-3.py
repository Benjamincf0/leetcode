class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0

        max_s = -10000

        l = r = 0

        for r in range(len(nums)):
            s+=nums[r]
            max_s = max(max_s, s)

            if s < 0:
                l = r+1
                s = 0

        return max_s