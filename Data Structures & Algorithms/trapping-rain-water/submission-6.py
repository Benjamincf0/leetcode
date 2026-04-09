import itertools
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        rightMax = 0
        leftMax = 0

        total=0
        while l<r:
            if rightMax < leftMax:
                total+= max(rightMax-height[r], 0)
                rightMax = max(height[r], rightMax)
                r-=1
            else:
                total+= max(leftMax-height[l], 0)
                leftMax = max(height[l], leftMax)
                l+=1
        return total