class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap)>=2:
            print(heap)
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            print(x, y)

            if y < x:
                heapq.heappush(heap, y-x)

        return -heap[0] if heap else 0