class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Time O(n) Space O(1)
        max_product = float("-inf")
        dp_max = 1
        dp_min = 1
        for r in range(len(nums)-1, -1, -1):
            dp_max, dp_min = max(nums[r], nums[r]*dp_max, nums[r]*dp_min), min(nums[r], nums[r]*dp_max, nums[r]*dp_min)
            max_product = max(max_product, dp_max)

        return max_product