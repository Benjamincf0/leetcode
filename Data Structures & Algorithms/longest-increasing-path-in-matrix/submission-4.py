class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        inDeg = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        q = deque()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
                    r2, c2 = r+dr, c+dc
                    if 0<=r2<len(matrix) and 0<=c2<len(matrix[0]) and matrix[r][c] > matrix[r2][c2]:
                        inDeg[r][c] += 1
                if inDeg[r][c] == 0: q.append((r,c,0))

        maxLen = 1
        while q:
            r, c, cur_len = q.popleft()
            maxLen = max(maxLen, 1+cur_len)

            for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
                r2, c2 = r+dr, c+dc
                if 0<=r2<len(matrix) and 0<=c2<len(matrix[0]) and matrix[r2][c2] > matrix[r][c]:
                    inDeg[r2][c2] -= 1
                    if inDeg[r2][c2] == 0:
                        q.append((r2, c2, 1+cur_len))

        return maxLen