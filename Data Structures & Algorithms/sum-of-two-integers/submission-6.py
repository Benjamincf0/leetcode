class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b != 0:
            c = (a&b)<<1 & mask
            a = (a ^ b) & mask
            b = c

        return a if a <= 0x7fffffff else ~(mask^a)