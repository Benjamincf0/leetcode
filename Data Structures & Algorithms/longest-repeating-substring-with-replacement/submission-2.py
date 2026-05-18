class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=r=0
        d = defaultdict(int) # frequency of each letter
        res = 0
        maxCount = 0 # frequency of most frequent char in current window

        while r < len(s):
            d[s[r]]+=1
            maxCount = max(maxCount, d[s[r]])
            len_window = r-l+1
            valid_window = len_window - maxCount <= k
            if valid_window:
                res = max(res, len_window)
                r+=1
            else:
                maxCount = 0
                d[s[l]]-=1
                l+=1
                if r<len(s): d[s[r]]-=1

        return res