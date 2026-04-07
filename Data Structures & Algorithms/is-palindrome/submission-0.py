class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        s = "".join(filter(str.isalnum, s))
        
        if s[0:len(s)//2:] == s[-1:(len(s)-1)//2:-1]: return True
        return False