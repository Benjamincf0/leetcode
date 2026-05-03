class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time O(n) Space O(n)
        l=r=0
        d = defaultdict(int) # frequency of each letter.
        res = 0 # len of max string with k permutations.
        maxCount = 0 # frequency of most frequent char in current window.

        while r < len(s):
            d[s[r]]+=1
            maxCount = max(maxCount, d[s[r]])
            len_window = r-l+1
            # a window is valid if we can make at most k mutations 
            # and obtain a 1 char string
            valid_window = len_window - maxCount <= k
            if valid_window:
                res = max(res, len_window)
                r+=1
            else:
                d[s[l]]-=1
                l+=1
                d[s[r]]-=1

        return res