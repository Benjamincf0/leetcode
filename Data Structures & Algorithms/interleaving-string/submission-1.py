class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3): return False

        cache = {}
        def dfs(i,j,k):
            if k == len(s3):
                return True

            if (i,j) in cache: return cache[(i,j)]
            if i<len(s1) and j<len(s2) and s1[i] == s2[j] == s3[k]:
                cache[(i,j)] = dfs(i+1,j,k+1) or dfs(i,j+1,k+1)
                return cache[(i,j)]
            if i < len(s1) and s1[i] == s3[k]:
                cache[(i,j)] = dfs(i+1,j,k+1)
                return cache[(i,j)]
            elif j < len(s2) and s2[j] == s3[k]:
                cache[(i,j)] = dfs(i,j+1,k+1)
                return cache[(i,j)]
            else:
                cache[(i,j)] = False
                return cache[(i,j)]

        return dfs(0,0,0)