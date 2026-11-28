import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cheapest_price = float("inf")
        dests = [[] for _ in range(n)]

        for from_i, to_i, price_i in flights:
            dests[from_i].append((to_i, price_i))

        visited = dict()

        pq = [(0, src, -1)]

        while pq:
            tot_price, from_i, i = heapq.heappop(pq)

            if from_i in visited and visited[from_i] < i: continue
            if from_i not in visited or i < visited[from_i]: visited[from_i] = i

            if from_i == dst:
                cheapest_price = min(cheapest_price, tot_price)
                continue

            if i == k:
                continue

            for to_i, price_i in dests[from_i]:
                heapq.heappush(pq, (tot_price+price_i, to_i, i+1))

        return cheapest_price if cheapest_price != float("inf") else -1