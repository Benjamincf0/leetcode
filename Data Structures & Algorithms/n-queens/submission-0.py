class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Time O(n!)

        res = []

        queens = []
        def dfs(c):
            r = len(queens)
            # check if valid pos
            for other_r, other_c in enumerate(queens):
                dr = abs(other_r-r)
                dc = abs(other_c-c)

                if dr == 0 or dc == 0 or dr == dc:
                    return

            queens.append(c)

            new_r = r+1
            if new_r < n:
                for new_c in range(0, n):
                    if new_c != c:
                        dfs(new_c)
            else:
                # save sln
                sln = []
                for col in queens:
                    s = "."*col+"Q"+"."*(n-col-1)
                    sln.append(s)
                res.append(sln)

            queens.pop()

        for c in range(n):
            dfs(c)

        return res