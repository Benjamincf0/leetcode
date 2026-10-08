class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(len(bin(n))):
            # basically we shift and extract the first bit...
            if ((n>>i) & 1):
                # 0001 -> 1000
                # starts with 1 and then shifts the 1 to the right spot..
                res |= (1 << (31-i))

        return res