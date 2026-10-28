class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Top down O(n*m) Space O(n*m)
        cache = {}
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2): return 0
            if (i, j) in cache: return cache[(i, j)]

            c1, c2 = text1[i], text2[j]
            if c1 == c2:
                cache[(i, j)] = 1 + dfs(i+1, j+1)
                return cache[(i, j)]
            else:
                cache[(i, j)] = max(dfs(i+1, j), dfs(i, j+1))
                return cache[(i, j)]

        return dfs(0, 0)