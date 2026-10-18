class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Time O(E*log(E)) or O(V^2*log(V)) Space O(V+E)
        if len(times) < n-1: return -1

        adj_list = [[] for _ in range(n+1)]

        for ui, vi, ti in times:
            adj_list[ui].append((ui, vi, ti))

        minheap = [(0, k)]
        visited = set()

        timer = 0
        while len(visited) < n and minheap:
            time, cur = heapq.heappop(minheap)
            if cur in visited: continue
            visited.add(cur)
            timer = time

            for _, vi, ti in adj_list[cur]:
                if vi not in visited:
                    heapq.heappush(minheap, (time+ti, vi))
                    

        return timer if len(visited) == n else -1