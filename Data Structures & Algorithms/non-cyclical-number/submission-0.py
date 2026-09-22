class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n not in s and n != 1:
            s.add(n)
            n = sum(map(lambda x: x*x, map(int, f"{n}")))

        return True if n == 1 else False