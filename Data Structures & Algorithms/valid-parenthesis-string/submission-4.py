class Solution:
    def checkValidString(self, s: str) -> bool:

        dp = [[False]*(len(s)//2 + 1) for i in range(len(s)+1)]

        dp[-1][0] = True

        for i in range(len(s)-1,-1,-1):
            for count in range(len(dp[i])):
                if s[i] == '(':
                    dp[i][count] = dp[i+1][count+1] if count+1 < len(s)//2 + 1 else False
                    # if we ever have count >= len(s)//2 + 1 => invalid
                elif s[i] == ')':
                    dp[i][count] = dp[i+1][count-1] if count-1 >= 0 else False
                    # if we ever have count < 0 => invalid
                else:
                    dp[i][count] = (dp[i+1][count-1] if count-1 >= 0 else False) \
                     or (dp[i+1][count+1] if count+1 < len(dp[i]) else False) \
                     or dp[i+1][count]
        
        # for _ in map(lambda row:print(list(map(lambda n:1 if n else 0,row))), dp):
        #     pass

        return dp[0][0]