class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        dp = [0]*len(s)

        for i, c in enumerate(reversed(t)):
            num_next_char_after_this_one = 0

            for j in range(len(s)-1, -1, -1):
                temp = dp[j]
                if s[j] == c:
                    if i == 0:
                        dp[j] = 1
                    else:
                        dp[j] = num_next_char_after_this_one
                else:
                    dp[j] = 0

                num_next_char_after_this_one += temp
            print(dp)

        return sum(dp)