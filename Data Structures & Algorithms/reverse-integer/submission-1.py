class Solution:
    def reverse(self, x: int) -> int:
        mask = (2**31)-1

        neg = -1 if x < 0 else 1
        x = abs(x)

        res = 0

        # i = 10**(int(math.log10(x)))
        i = 10
        while x > 0:
            remainder = x % 10
            x = x // 10
            if res > mask//10:
                return 0
            elif res == mask//10 and remainder > mask%10:
                return 0
            res = res*10+remainder
            # print(res)

        return neg*res