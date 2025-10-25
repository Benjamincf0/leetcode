# easy
# 3461. Check If Digits Are Equal in String After Operations I
# this is faster because list comprehension runs in C and ord() is faster than int().
# convert string to list, then run loops
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s_list = [ord(c) - ord('0') for c in s]
        n = len(s)
        while len(s_list) > 2:
            s_list = [((s_list[i] + s_list[i+1]) % 10) for i in range(len(s_list) - 1)]
        return s_list[0] == s_list[1]
