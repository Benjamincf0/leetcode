class Solution:
    def climbStairs(self, n: int) -> int:
        n += 1

        s5 = math.sqrt(5)
        
        return int((1/s5)*(((1+s5)/2)**n - ((1-s5)/2)**n))