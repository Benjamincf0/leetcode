class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        s = set([i for i in range(n)])
        adj_list = defaultdict(list)

        for f, t in edges:
            adj_list[f].append(t)
            adj_list[t].append(f)

        num = 0

        q = deque()

        while s:
            first = s.pop()
            q.append(first)

            # visit set
            while q:
                cur = q.pop()
                s.discard(cur)

                for child in adj_list[cur]:
                    if child in s:
                        q.append(child)


            num += 1

        return num