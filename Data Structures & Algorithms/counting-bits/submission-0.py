class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            tot = 0
            while i > 0:
                tot += i % 2
                i //= 2

            res.append(tot)

        return res