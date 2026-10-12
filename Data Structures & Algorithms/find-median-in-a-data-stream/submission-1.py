class MedianFinder:

    def __init__(self):
        self.maxheap = [] # bottom half
        self.minheap = [] # upper half
        self.median = float("inf") # midpoint

    def addNum(self, num: int) -> None:
        if num < self.median:
            heapq.heappush(self.maxheap, -1*num)
        else:
            heapq.heappush(self.minheap, num)

        # check if we need to rebalance
        if len(self.maxheap) > len(self.minheap)+1:
            popped = -1*heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, popped)
        elif len(self.minheap) > len(self.maxheap)+1:
            popped = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -1*popped)

        if len(self.maxheap) > len(self.minheap):
            self.median = -1*self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            self.median = self.minheap[0]
        else:
            self.median = (self.minheap[0] + -1*self.maxheap[0])/2

    def findMedian(self) -> float:
        return self.median

# max = 1 
# min = 3 
# median = 1 