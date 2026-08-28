class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = range(len(board))
        COLS = range(len(board[0]))
        
        count = 0
        def dfs(c, r, count):
            
            if count == len(word):
                return True

            if c not in COLS \
            or r not in ROWS:
                return False

            if word[count] != board[r][c]:
                return False
            
            board[r][c] = None
            count += 1

            out = any((
                dfs(c-1, r, count),
                dfs(c+1, r, count),
                dfs(c, r-1, count),
                dfs(c, r+1, count)))

            count -= 1
            board[r][c] = word[count]

            return out

        return any(dfs(c, r, count) for c in COLS for r in ROWS)