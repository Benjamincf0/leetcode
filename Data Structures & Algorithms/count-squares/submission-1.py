class CountSquares:

    def __init__(self):
        self.rows = defaultdict(set)
        self.columns = defaultdict(set)
        self.pointCounts = defaultdict(int)

    def add(self, point: list[int]) -> None:
        r, c = point
        point = (r, c)
        self.rows[r].add(point)
        self.columns[c].add(point)
        self.pointCounts[point] += 1

    def count(self, point: list[int]) -> int:
        x, y = point
        count = 0
        for _, c in self.rows[x]:
            for r, _ in self.columns[y]:
                if (r, c) in self.pointCounts and abs(r-x) == abs(y-c) > 0:
                    # we gottem
                    count += self.pointCounts[(x, c)] * \
                             self.pointCounts[(r, y)] * \
                             self.pointCounts[(r, c)]

        return count

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)