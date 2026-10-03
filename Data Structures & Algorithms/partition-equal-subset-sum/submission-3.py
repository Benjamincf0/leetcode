from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0: return False
        target = sum(nums)//2

        sums = set([0])
        
        for n in nums[::-1]:
            for s in tuple(sums):
                if s+n == target: return True
                sums.add(s+n)

        return False

# [1 2 3 4] t=5
# {0 4 3 7 2 6 5}