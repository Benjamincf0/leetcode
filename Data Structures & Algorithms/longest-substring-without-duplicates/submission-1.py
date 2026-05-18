class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        i=0
        while i < len(s): # O(n^2)
            hs = set()
            j = i
            length = 0
            while j<len(s) and s[j] not in hs:
                hs.add(s[j])
                length+=1
                j+=1
            maxLength = max(length, maxLength)
            i = j
        return maxLength