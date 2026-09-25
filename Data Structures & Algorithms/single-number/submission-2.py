class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cum = 0
        for i in range(len(nums)):
            cum ^= nums[i]

        return cum