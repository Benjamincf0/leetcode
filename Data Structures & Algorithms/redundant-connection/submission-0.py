class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(a):
            if a == parents[a]:
                return a
            
            res = find(parents[a])
            parents[a] = res

            return res

        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1 == p2:
                return False

            if rank[p1] < rank[p2]:
                parents[p1] = p2
                rank[p2] += rank[p1]
            else:
                parents[p2] = p1
                rank[p1] += rank[p2]

            return True



        for a, b in edges:
            if not union(a, b):
                return [a, b]