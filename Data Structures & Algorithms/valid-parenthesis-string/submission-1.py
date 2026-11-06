class Solution:
    def checkValidString(self, s: str) -> bool:

        memo = {}

        def dfs(i, count):
            if i == len(s) and count == 0:
                return True
            elif count < 0 or i == len(s):
                return False

            if (i, count) in memo:
                return memo[(i, count)]

            if s[i] == '(':
                memo[(i, count)] = dfs(i+1, count+1)
            elif s[i] == ')':
                memo[(i, count)] = dfs(i+1, count-1)
            else:
                memo[(i, count)] = dfs(i+1, count) or dfs(i+1, count+1) or dfs(i+1, count-1)

            return memo[(i, count)]

        return dfs(0,0)