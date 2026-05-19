class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = ord('a')

        ls = [0]*26
        lt = [0]*26

        for c in s:
            ls[ord(c)-a]+=1
        
        for c in t:
            lt[ord(c)-a]+=1

        return ls == lt