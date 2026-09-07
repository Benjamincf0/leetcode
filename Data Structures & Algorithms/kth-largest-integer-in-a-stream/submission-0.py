class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [-i for i in nums]
        heapq.heapify(self.heap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        k_nums = [heapq.heappop(self.heap) for _ in range(self.k)]
        for n in k_nums: heapq.heappush(self.heap, n)
        return -k_nums[-1]