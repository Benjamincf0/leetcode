class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i, row in enumerate(board):
            for j, item in enumerate(row):
                if item == ".": continue

                box_idx = 3*(i//3) + j//3
                if item in rows[i] | cols[j] | boxes[box_idx]: return False
                rows[i].add(item)
                cols[j].add(item)
                boxes[box_idx].add(item)
        return True