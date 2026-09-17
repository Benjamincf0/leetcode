class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(int)
        for i, c in enumerate(s): d[c] = i

        res = []
        prev_split = -1
        next_split = 0
        for i, c in enumerate(s):
            next_split = max(next_split, d[c])

            if i == next_split:
                res.append(next_split-prev_split)
                prev_split = next_split

        return res