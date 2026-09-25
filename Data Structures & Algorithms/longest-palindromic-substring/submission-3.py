class Solution:
    def longestPalindrome(self, s: str) -> str:
        ml = 0
        mr = 0

        for i in range(len(s)):
            l = i
            r = i
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            if r-l-1 > mr - ml+1:
                ml = l+1
                mr = r-1


            l = i
            r = i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-1 > mr - ml+1:
                ml = l+1
                mr = r-1

        return s[ml:mr+1]