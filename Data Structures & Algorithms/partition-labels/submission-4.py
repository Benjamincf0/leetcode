class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(int)
        for c in s: d[c] += 1

        num_complete_letters = 0
        distinct_letters = set()
        res = []

        prev = -1
        for i, c in enumerate(s):
            distinct_letters.add(c)
            d[c] -= 1
            if d[c] == 0:
                # this letter is complete
                num_complete_letters += 1

            if num_complete_letters == len(distinct_letters):
                res.append(i-prev)
                prev = i

        return res