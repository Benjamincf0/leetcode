class Solution:
    def hammingWeight(self, n: int) -> int:
        tot = 0
        while n > 0:
            tot += n % 2
            n //= 2

        return tot