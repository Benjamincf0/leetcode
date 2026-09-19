"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def clone(nd):
            if nd in oldToNew:
                return oldToNew[nd]
            elif nd is None: return None

            copy = Node(nd.val)
            oldToNew[nd] = copy

            for nei in nd.neighbors:
                copy.neighbors.append(clone(nei))

            return copy

        return clone(node)