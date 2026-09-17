class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(int)
        for c in s: d[c] += 1

        cur = defaultdict(int)
        complete = 0
        res = []

        prev = -1
        for i, c in enumerate(s):
            cur[c] += 1
            if cur[c] == d[c]:
                # this letter is complete
                complete += 1

            if complete == len(cur):
                res.append(i-prev)
                prev = i

        return res