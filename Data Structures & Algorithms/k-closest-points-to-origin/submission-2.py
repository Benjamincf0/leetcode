class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ds = defaultdict(list)

        for i, (x, y) in enumerate(points):
            d = x**2+y**2
            ds[d].append(i)

        heap = []
        for key, ps in ds.items():
            for _ in ps: heap.append(key)

        heapq.heapify(heap)

        res = []

        for _ in range(k):
            min_distance = heapq.heappop(heap)
            point_index = ds[min_distance].pop()
            res.append(points[point_index])

        return res