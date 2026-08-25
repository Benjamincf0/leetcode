class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Time O(V+E) ; Space O(V+E)

        d = defaultdict(list)

        for a, b in edges:
            d[a].append(b)
            d[b].append(a)

        root = 0

        visited = set()
        q = deque()
        q.append((root, -1))

        while q:
            node, prev_node = q.popleft()

            # if there's a cycle, we'll end up with the same node added twice to the queue.
            if node in visited:
                return False
            
            visited.add(node)

            children = d[node]
            for c in children:
                if c != prev_node:
                    q.append((c, node))

        is_connected_graph = len(visited) == n
        return is_connected_graph