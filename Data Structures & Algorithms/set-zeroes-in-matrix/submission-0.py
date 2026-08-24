class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = range(len(matrix))
        cols = range(len(matrix[0]))

        zero_rows = set()
        zero_cols = set()

        for i in rows:
            for j in cols:
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for row in zero_rows:
            matrix[row] = [0 for _ in cols]

        for col in zero_cols:
            for i in rows:
                matrix[i][col] = 0
