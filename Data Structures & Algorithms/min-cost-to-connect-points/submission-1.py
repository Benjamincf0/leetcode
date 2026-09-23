class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # Prim's algorithm O(n^2 * logn)
        visited = set()
        minheap = [(0, tuple(points[0]))]
        cost = 0

        while len(visited) < len(points):
            min_d, pt = heapq.heappop(minheap)
            if pt in visited: continue
            cost += min_d
            visited.add(pt)

            for nb in points:
                if tuple(nb) in visited: continue
                d = abs(nb[0]-pt[0])+abs(nb[1]-pt[1])
                heapq.heappush(minheap, (d, tuple(nb)))

        return cost
        