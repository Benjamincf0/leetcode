class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rs = range(len(grid))
        cs = range(len(grid[0]))

        visited = set()
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        d = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = d
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if r+dr in rs and \
                        c+dc in cs and \
                        (r+dr, c+dc) not in visited and \
                        grid[r+dr][c+dc] == 2**31-1:
                            q.append((r+dr, c+dc))
                            visited.add((r+dr, c+dc))
            d += 1