class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Time O(len(s)+len(t)) ; Space O(len(set(t)))
        # Two pointers
        letters = {c:0 for c in t}
        for c in t: letters[c]+=1

        print(letters)
        l = r = 0

        min_l = min_r = None

        n_remaining = len(t)
        for r in range(len(s)):
            rc = s[r]
            lc = s[l]
            print()

            if rc in letters:
                letters[rc]-=1

                if letters[rc] >= 0:
                    n_remaining -= 1
                    
                    while n_remaining == 0 and l < len(s):
                        lc = s[l]
                        if min_l is None or min_r-min_l>r-l:
                            min_l = l
                            min_r = r
    
                        if lc in letters:
                            letters[lc]+=1
                            if letters[lc] > 0:
                                n_remaining+=1
                            
    
                        l+=1

        if min_l is None:
            return ''
        return s[min_l:min_r+1]