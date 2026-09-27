class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(map(int, list(bin(n)[2:])))