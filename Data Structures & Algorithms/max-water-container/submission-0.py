class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0

        l=0
        r=len(heights)-1
        while l < r:
            a = (r-l)*min(heights[l], heights[r])
            if a > m: m=a
            elif heights[l] > heights[r]:
                r-=1
            elif heights[l] < heights[r]:
                l+=1
            else:
                r-=1
                l+=1
        return m