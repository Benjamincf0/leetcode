class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rectStack = [] # [ [rectStart, rectHeight], ...]
        maxArea = 0

        for i, currHeight in enumerate(heights):

            newRectStart = i
            while rectStack and rectStack[-1][1] > currHeight:
                rectStart, rectHeight = rectStack.pop()
                prevRectArea = (i-rectStart)*rectHeight
                maxArea = max(maxArea, prevRectArea)
                newRectStart = rectStart
            rectStack.append([newRectStart, currHeight])
        
        return max(max([(len(heights)-rectStart)*rectHeight for rectStart, rectHeight in rectStack]), maxArea)