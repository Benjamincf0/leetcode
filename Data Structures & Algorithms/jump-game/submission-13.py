class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Bottom-up DP greedy strategy Time O(n) & Space O(1)
        r = len(nums)-1

        while r > 0:
            l = r - 1
            while l > -1 and l + nums[l] < r:
                l-=1

            if l == -1: return False

            r = l

        return True