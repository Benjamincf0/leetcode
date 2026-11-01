from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        can_flow_to_pacific = set()
        can_flow_to_atlantic = set()
        can_flow_to_both = set()

        q = deque()

        for i in range(len(heights)):
            q.append((i, 0))
        for i in range(len(heights[0])):
            q.append((0, i))

        while q:
            r, c = q.pop()
            can_flow_to_pacific.add((r,c))

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                r2,c2 = r+dr,c+dc

                if 0<=r2<len(heights) and 0<=c2<len(heights[0]) \
                    and (r2,c2) not in can_flow_to_pacific \
                    and heights[r][c] <= heights[r2][c2]:
                    q.append((r2,c2))

        for i in range(len(heights)):
            q.append((i, len(heights[0])-1))
        for i in range(len(heights[0])):
            q.append((len(heights)-1, i))

        while q:
            r, c = q.pop()
            can_flow_to_atlantic.add((r,c))

            if (r,c) in can_flow_to_pacific:
                can_flow_to_both.add((r,c))

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                r2,c2 = r+dr,c+dc

                if 0<=r2<len(heights) and 0<=c2<len(heights[0]) \
                    and (r2,c2) not in can_flow_to_atlantic \
                    and heights[r][c] <= heights[r2][c2]:
                    q.append((r2,c2))

        return list(can_flow_to_both)