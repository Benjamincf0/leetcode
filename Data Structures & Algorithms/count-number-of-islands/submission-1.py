class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time O(n*m) ; Space O(n*m)
        num_islands = 0

        def dfs(i, j):
            if (not (0<=i<len(grid)) or \
                not (0<=j<len(grid[0])) or \
                grid[i][j] == "visited"):
                return 0

            is_land = grid[i][j] == "1"
            grid[i][j] = "visited"

            if is_land:
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)
                return 1
            else:
                return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                num_islands += dfs(i, j)

        return num_islands