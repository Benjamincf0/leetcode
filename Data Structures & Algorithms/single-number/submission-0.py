class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cum = nums[0]
        for i in range(1, len(nums)):
            cum ^= nums[i]

        return cum