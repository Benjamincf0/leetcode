from functools import cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        rs = range(len(s))

        @cache
        def dfs(i, j):
            if i not in rs or j not in rs or s[i] != s[j]:
                return None

            can_grow = dfs(i-1, j+1)
            if can_grow:
                return can_grow
            else:
                return i, j

        mij = (0, 0)
        for i in rs:
            res = dfs(i, i)
            if res and res[1]-res[0] > mij[1]-mij[0]:
                mij = res

        for i in rs[:-1]:
            res = dfs(i, i+1)
            if res and res[1]-res[0] > mij[1]-mij[0]:
                mij = res

        return s[mij[0]: mij[1]+1]