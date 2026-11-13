class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        def dfs(i, j):
            if (i,j) in memo: return memo[(i,j)]
            maxLen = 0
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                i2, j2 = i+di, j+dj
                
                if 0 <= i2 < len(matrix) and 0 <= j2 < len(matrix[0]) and matrix[i][j] < matrix[i2][j2]:
                    maxLen = max(maxLen, 1+dfs(i2,j2))

            memo[(i,j)] = maxLen
            return maxLen

        return 1+max(dfs(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if (i,j) not in memo)