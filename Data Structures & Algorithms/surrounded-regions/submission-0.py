class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        HEIGHT = len(board)
        WIDTH = len(board[0])

        q = deque()

        for r in range(HEIGHT):
            if board[r][0] == 'O':
                q.append((r, 0))
            if board[r][WIDTH-1] == 'O':
                q.append((r, WIDTH-1))

        for c in range(1, WIDTH-1):
            if board[0][c] == 'O':
                q.append((0, c))
            if board[HEIGHT-1][c] == 'O':
                q.append((HEIGHT-1, c))

        while q:
            r, c = q.popleft()
            board[r][c] = 'B'

            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if (0 <= nr < HEIGHT) and (0 <= nc < WIDTH) and board[nr][nc] == 'O':
                    q.append((nr, nc))

        for r in range(HEIGHT):
            for c in range(WIDTH):
                if board[r][c] == 'B':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'