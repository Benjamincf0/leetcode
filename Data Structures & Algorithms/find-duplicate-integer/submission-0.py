class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = set()
        for num in nums:
            if num in d: return num
            d.add(num)