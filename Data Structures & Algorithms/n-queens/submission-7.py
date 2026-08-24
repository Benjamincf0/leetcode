class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Time O(n*n!) ; Space O(n^2)

        res = []
        queens = []

        other_cols = set()
        other_pos_diag = set()
        other_neg_diag = set()
        def dfs(c):
            r = len(queens)
            # check if in check O(1)
            same_col = c in other_cols
            same_pos_diag = (r-c) in other_pos_diag
            same_neg_diag = (r+c) in other_neg_diag
            if same_col or same_pos_diag or same_neg_diag: return

            queens.append(c)
            other_pos_diag.add(r-c)
            other_neg_diag.add(r+c)
            other_cols.add(c)

            new_r = r+1
            if new_r < n:
                for new_c in range(0, n):
                    dfs(new_c)
            else:
                # save sln
                sln = []
                for col in queens:
                    s = "."*col+"Q"+"."*(n-col-1)
                    sln.append(s)
                res.append(sln)

            queens.pop()
            other_pos_diag.remove(r-c)
            other_neg_diag.remove(r+c)
            other_cols.remove(c)

        for c in range(n):
            dfs(c)

        return res