class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Time O(log(n)) Space O(log(n))
        if n == 0: return 1
        elif n == 1: return x
        if n < 0:
            n = - n
            x = 1 / x
        p = self.myPow(x, n // 2)
        rest = x if n % 2 == 1 else 1
        return p*p * rest
