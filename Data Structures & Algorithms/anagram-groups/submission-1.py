class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gd = defaultdict(list)
        a = ord('a')

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-a] +=1

            gd[tuple(count)].append(s)
        return list(gd.values())