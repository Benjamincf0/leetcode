class Solution:
    cache = dict()
    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        elif n == 0:
            return 1
        elif n < 0:
            return 0

        val = self.climbStairs(n-1)+self.climbStairs(n-2)
        self.cache[n] = val
        return val