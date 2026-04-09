#import itertools
class Solution:
    def trap(self, height: List[int]) -> int:
        # this might be gay but it works lmao
        left = list(itertools.accumulate(height, max))
        right = list(itertools.accumulate(height[::-1], max))
        
        accumulation = 0
        for l, h in enumerate(height):
            r = len(height)-l-1
            # instead of using l-1 and r+1, im just using l and r, which yields the same result logically and removes the need for maxing with 0, and checking start and end...
            accumulation += min(left[l], right[r]) - h
        return accumulation