class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        minHeap = [(grid[0][0], (0, 0))]
        visited = {(0, 0)}

        while minHeap:
            maxHeight, (x, y) = heapq.heappop(minHeap)
            # print("visiting", x,y)

            if (x,y) == (len(grid[0])-1, len(grid)-1):
                return maxHeight

            for dx, dy in ((-1, 0),(1, 0),(0,-1),(0,1)):
                x2, y2 = x+dx, y+dy

                if 0<=x2<len(grid[0]) and 0<=y2<len(grid) and \
                    (x2, y2) not in visited:
                    height = grid[y2][x2]
                    visited.add((x2,y2))
                    heapq.heappush(minHeap, (max(maxHeight,height), (x2,y2)))

        return -1