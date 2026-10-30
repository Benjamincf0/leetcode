class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3): return False

        cache = {}
        def dfs(i,j,k):
            if k == len(s3):
                return True

            if (i,j,k) in cache: return cache[(i,j,k)]
            if i<len(s1) and j<len(s2) and s1[i] == s2[j] == s3[k]:
                cache[(i,j,k)] = dfs(i+1,j,k+1) or dfs(i,j+1,k+1)
                return cache[(i,j,k)]
            if i < len(s1) and s1[i] == s3[k]:
                cache[(i,j,k)] = dfs(i+1,j,k+1)
                return cache[(i,j,k)]
            elif j < len(s2) and s2[j] == s3[k]:
                cache[(i,j,k)] = dfs(i,j+1,k+1)
                return cache[(i,j,k)]
            else:
                cache[(i,j,k)] = False
                return cache[(i,j,k)]

        return dfs(0,0,0)