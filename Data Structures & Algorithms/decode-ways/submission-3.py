class Solution:
    def numDecodings(self, s: str) -> int:

        cache = {}

        def dfs(i):
            if i == len(s): return 1
            elif s[i] == '0': return 0

            if i in cache: 
                return cache[i]

            if i+1 < len(s) and int(s[i:i+2]) < 27:
                cache[i] = dfs(i+2)+dfs(i+1)
            else: cache[i] = dfs(i+1)

            return cache[i]

        out = dfs(0)
        # print(*(dfs(i) for i in range(len(s))))

        return out