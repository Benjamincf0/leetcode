class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ds = defaultdict(list)

        for x, y in points:
            d = x**2+y**2
            ds[d].append([x, y])

        heap = []
        for key, points in ds.items():
            for _ in points: heap.append(key)

        heapq.heapify(heap)

        res = []

        for _ in range(k):
            min_distance = heapq.heappop(heap)
            point = ds[min_distance].pop()
            res.append(point)

        return res