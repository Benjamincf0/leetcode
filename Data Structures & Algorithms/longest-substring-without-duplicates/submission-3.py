class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        hs = set()
        i=j=0
        while j < len(s):
            if s[j] not in hs:
                hs.add(s[j])
                j+=1
            else:
                hs.remove(s[i])
                i+=1

            maxLength = max(maxLength, j-i)

        return maxLength