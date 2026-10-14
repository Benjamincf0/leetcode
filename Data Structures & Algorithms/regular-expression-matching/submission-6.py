from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            if i == len(s):
                return j + 1 < len(p) and p[j+1] == '*' and dfs(i, j+2)

            repeats = j < len(p)-1 and p[j+1] == '*'
            if p[j] == '.':
                if repeats:
                    return dfs(i+1, j) or dfs(i, j+2)
                else:
                    return dfs(i+1, j+1)
            else:
                if repeats:
                    return ((s[i] == p[j]) and dfs(i+1, j)) or dfs(i, j+2)
                else:
                    return (s[i] == p[j]) and dfs(i+1, j+1)

        return dfs(0, 0)