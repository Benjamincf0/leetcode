class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Merry Kirkmass
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break

        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast: break

        return slow