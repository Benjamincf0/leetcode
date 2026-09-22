class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Time O(log(n)) Space O(1)
        if n < 0:
            x = 1 / x
            n = -n
        if n == 0: return 1
        elif n == 1: return x

        tot = 1
        while n > 0:
            if n == 1: return tot*x
            i = 1
            res = x
            while 2*i <= n:
                res *= res
                i *= 2
            n -= i
            tot *= res

        return tot