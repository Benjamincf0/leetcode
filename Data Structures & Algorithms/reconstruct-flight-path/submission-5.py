class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)

        for from_i, to_i in tickets:
            d[from_i].append(to_i)

        for k in d.keys():
            d[k].sort(reverse=True)
            # so we can pop smallest lexical from left.

        res = []

        def dfs(node):
            while d[node]:
                dfs(d[node].pop())
            res.append(node)

        dfs("JFK")
        return res[::-1]