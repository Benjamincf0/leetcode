class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time O(n) Space O(n)
        l=0
        d = defaultdict(int) # frequency of each letter in current window.
        res = 0 # len of max string with k permutations.

        for r in range(len(s)):
            d[s[r]]+=1
            # a window is valid if we can make at most k mutations 
            # and obtain a 1 char string
            valid_window = r-l+1 - max(d.values()) <= k
            if not valid_window:
                d[s[l]]-=1
                l+=1
            
            res = max(res, r-l+1)

        return res