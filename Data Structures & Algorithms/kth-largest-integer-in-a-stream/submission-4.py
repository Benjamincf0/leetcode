class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Finding the kth largest element is
        # equivalent to finding the smallest
        # element when the stream consists only
        # of the k largest elements..
        # i.e. we use a min-heap of size k.
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k: heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap)>self.k:
            heapq.heappop(self.heap) # to maintain the size of k
        return self.heap[0]