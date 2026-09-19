class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        cache = {}

        def dfs(i, j):
            if j == len(t) or i == len(s): return 0
            if len(s)-i < len(t)-j: return 0
            if s[i] != t[j]: return 0

            if j == len(t)-1:
                return 1

            if (i, j) in cache: return cache[(i, j)]

            cache[(i, j)] = sum(dfs(k, j+1) for k in range(i+1, len(s)))
            return cache[(i, j)]

        return sum(dfs(k, 0) for k in range(len(s)))