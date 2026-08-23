class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = range(len(grid))
        cols = range(len(grid[0]))

        def bfs(i, j) -> float:
            q = deque()

            q.append((i, j))

            area = 0

            while len(q) > 0:
                i, j = q.popleft()
                if (i not in rows) or (j not in cols) or grid[i][j] == 0:
                    continue

                grid[i][j] = 0

                area += 1

                q.append((i-1, j))
                q.append((i+1, j))
                q.append((i, j-1))
                q.append((i, j+1))

            return area


        for i in rows:
            for j in cols:
                max_area = max(max_area, bfs(i, j))

        return max_area