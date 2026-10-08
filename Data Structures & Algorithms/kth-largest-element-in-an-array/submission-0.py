class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-1*i for i in nums]

        heapq.heapify(heap)

        for i in range(k-1):
            heapq.heappop(heap)

        return -1*heapq.heappop(heap)