class MedianFinder:

    def __init__(self):
        self.maxheap = [] # bottom half
        self.minheap = [] # upper half

    def addNum(self, num: int) -> None:
        if num < self.findMedian():
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

    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap) == 0: return float("-inf")
        if len(self.maxheap) > len(self.minheap):
            return -1*self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return (self.minheap[0] + -1*self.maxheap[0])/2