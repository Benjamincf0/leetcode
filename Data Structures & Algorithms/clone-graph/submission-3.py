"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return
        visited : set[int] = set()
        al = defaultdict(list)
        q = deque()
        q.append(node)
        visited.add(node.val)

        while q:
            cur_node = q.pop()

            for nb in cur_node.neighbors:
                al[cur_node.val].append(nb.val)
                if nb.val not in visited:
                    q.append(nb)
                    visited.add(nb.val)

        l = [Node(i) for i in range(1, len(al)+1)]

        for i, nbs in al.items():
            for nb_val in nbs:
                l[i-1].neighbors.append(l[nb_val-1])

        return l[node.val-1] if l else Node(node.val)