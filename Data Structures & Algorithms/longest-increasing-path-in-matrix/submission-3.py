class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[None]*len(matrix[0]) for _ in range(len(matrix))]

        def dfs(r, c):
            if dp[r][c] is not None:
                return dp[r][c]

            dp[r][c] = 1
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r2, c2 = r+dr, c+dc
                if 0<=r2<len(matrix) and 0<=c2<len(matrix[0]) and matrix[r][c] < matrix[r2][c2]:
                    dp[r][c] = max(dp[r][c], 1+dfs(r2, c2))

            return dp[r][c]

        return max(dfs(r, c) for r in range(len(matrix)) for c in range(len(matrix[0])))