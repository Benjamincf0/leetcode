class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Top-down DP - Time O() Space O()
        dp = [False]*(len(s)+1)
        dp[-1] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if i+len(word)-1 < len(s) and s[i: i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                if dp[i]: break

        return dp[0]