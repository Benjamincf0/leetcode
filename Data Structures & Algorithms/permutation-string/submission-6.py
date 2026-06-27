class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for letter in s1:
            if letter in s1_map:
                s1_map[letter] += 1
            else:
                s1_map[letter] = 1

        l = 0
        while l <= len(s2)-len(s1):
            r = l+len(s1)
            hm = defaultdict(int)
            for i in range(l, r):
                letter = s2[i]
                hm[letter]+=1
                if letter not in s1_map:
                    l+=i-l
                    break
            l+=1
            if hm == s1_map: return True
        
        return False