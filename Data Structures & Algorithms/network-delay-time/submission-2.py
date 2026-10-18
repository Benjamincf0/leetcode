class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if len(times) < n-1: return -1

        adj_list = [[] for _ in range(n+1)]

        for ui, vi, ti in times:
            adj_list[ui].append((ui, vi, ti))

        # for i in range(1, n+1):
        #     adj_list[i].sort(key=lambda x: x[2])

        # print(adj_list)

        minheap = [(0, k)]
        visited = set()

        timer = 0
        while minheap:
            time, cur = heapq.heappop(minheap)
            if cur in visited: continue
            visited.add(cur)
            # print("we visited", cur, "in", time, "seconds.")
            timer = time

            for _, vi, ti in adj_list[cur]:
                if vi not in visited:
                    heapq.heappush(minheap, (time+ti, vi))


            # print(minheap, visited)
                    

        return timer if len(visited) == n else -1