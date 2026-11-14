class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        heap = [-c for c in Counter(tasks).values()]
        heapq.heapify(heap)

        q = deque()
        time = 0
        while heap or q:
            time += 1
            if heap:
                cnt = heapq.heappop(heap)+1
                if cnt:
                    # will be available to process in n cycles.
                    q.append((cnt, time+n))
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time