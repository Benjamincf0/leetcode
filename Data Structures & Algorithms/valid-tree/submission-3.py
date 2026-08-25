class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # First convert to a hashmap: dict[node, list[node]]
        # BFS/DFS using a set to check for already visited nodes
        # which would imply a cycle.

        d = defaultdict(list)

        for a, b in edges:
            d[a].append(b)
            d[b].append(a)

        root = 0

        s = set()
        q = deque()
        q.append(root)

        while q:
            node = q.pop()
            if node in s:
                return False
            
            s.add(node)

            children = d[node]
            for c in children:
                if c not in s:
                    q.append(c)

        is_connected_graph = len(s) == n
        return is_connected_graph