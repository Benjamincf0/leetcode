class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        l = len(nums)
        return (((l+1)*(l))//2) - sum(nums)