class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Time O(n*m) ; Space O(n+m)
        rows = range(len(matrix))
        cols = range(len(matrix[0]))

        row_0_is_zero = False

        for r in rows:
            for c in cols:
                if matrix[r][c] == 0:
                    if r == 0:
                        row_0_is_zero = True
                    else:
                        matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in rows[1:]:
            row_is_zero = matrix[r][0] == 0

            for c in cols[1:]:
                col_is_zero = matrix[0][c] == 0
                if row_is_zero or col_is_zero:
                    matrix[r][c] = 0

        col_0_is_zero = matrix[0][0] == 0
        if col_0_is_zero:
            for i in rows: matrix[i][0] = 0

        if row_0_is_zero:
            for i in cols: matrix[0][i] = 0