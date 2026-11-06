class Solution:
    def checkValidString(self, s: str) -> bool:

        dp = [[False]*(len(s)) for i in range(len(s)+1)]

        dp[-1][0] = True

        for i in range(len(s)-1,-1,-1):
            for j in range(len(dp[i])):
                if s[i] == '(':
                    dp[i][j] = dp[i+1][j+1] if j+1 < len(dp[i]) else False
                elif s[i] == ')':
                    dp[i][j] = dp[i+1][j-1] if j-1 >= 0 else False
                else:
                    dp[i][j] = (dp[i+1][j-1] if j-1 >= 0 else False) \
                     or (dp[i+1][j+1] if j+1 < len(dp[i]) else False) \
                     or dp[i+1][j]
        
        # for _ in map(lambda row:print(list(map(lambda n:1 if n else 0,row))), dp):
        #     pass

        return dp[0][0]