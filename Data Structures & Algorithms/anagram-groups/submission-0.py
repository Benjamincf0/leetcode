class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gd = {}
        a = ord('a')

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-a] +=1
            count = tuple(count)

            if count in gd:
                gd[count].append(s)
            else:
                gd[count] = [s]

        return list(gd.values())