class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # easy peasy
        # Time O(n*m) ; Space O(n*m)
        max_area = 0
        rows = range(len(grid))
        cols = range(len(grid[0]))

        def bfs(i, j) -> int:
            q = deque()

            q.append((i, j))

            area = 0

            while len(q) > 0:
                i, j = q.popleft()
                if (i not in rows) or (j not in cols) or grid[i][j] == 0:
                    continue

                grid[i][j] = 0

                area += 1

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + dr, j + dc
                    if ni in rows and nj in cols and grid[ni][nj] == 1:
                        q.append((ni, nj))

            return area


        for i in rows:
            for j in cols:
                max_area = max(max_area, bfs(i, j))

        return max_area