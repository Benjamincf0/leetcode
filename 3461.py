# easy
# 3461. Check If Digits Are Equal in String After Operations I
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            s_new = ""
            for i in range(len(s) - 1):
                res = (int(s[i]) + int(s[i+1])) % 10
                s_new += str(res)
            
            s = s_new
        return s[0] == s[1]
