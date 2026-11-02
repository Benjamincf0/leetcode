class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(l, r):
            if l == len(word1) and r == len(word2):
                return 0
            elif l == len(word1):
                return len(word2)-r
            elif r == len(word2):
                return len(word1)-l

            if (l,r) in memo: return memo[(l,r)]
            
            if word1[l] == word2[r]:
                memo[(l,r)] = dfs(l+1,r+1)
            else:
                memo[(l,r)] = min(1+dfs(l+1,r+1), # replace
                           1 + dfs(l+1,r), # delete
                           1 + dfs(l,r+1)  # insert
                           )

            return memo[(l,r)]

        return dfs(0,0)