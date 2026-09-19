class Solution:
    def countSubstrings(self, s: str) -> int:
        # num_palindromes_centered_at_i
        dp = [0]*len(s)

        for i in range(len(s)-1, -1, -1):
            l = r = i
            while 0 <= l and r < len(s):
                if s[l] == s[r]:
                    dp[i] += 1
                    l -= 1
                    r += 1
                else:
                    break

            l, r = i, i+1
            while 0 <= l and r < len(s):
                if s[l] == s[r]:
                    dp[i] += 1
                    l -= 1
                    r += 1
                else:
                    break

        return sum(dp)   