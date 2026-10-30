class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        cols, rows = len(matrix[0]), len(matrix)
        for radc, radr in zip(range(cols//2),range(rows//2)):
            res.extend(matrix[radr][radc:cols-radc])
            res.extend(map(lambda x: x[cols-radc-1], matrix[radr+1:rows-radr-1]))

            res.extend(reversed(matrix[rows-radr-1][radc:cols-radc]))
            res.extend(map(lambda x: x[radc], reversed(matrix[radr+1:rows-radr-1])))

        if rows >= cols and cols % 2 == 1:
            res.extend(map(lambda x:x[cols//2], matrix[cols//2:rows-(cols//2)]))
        elif cols >= rows and rows % 2 == 1:
            res.extend(matrix[rows//2][rows//2:cols-(rows//2)])

        return res