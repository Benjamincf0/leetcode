class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp_cur = [0]*(len(word2)+1)
        dp_prev = [0]*(len(word2)+1)

        for j in range(len(dp_prev)):
            dp_prev[j] = len(word2)-j

        for i in range(len(word1)-1,-1,-1):
            dp_cur[-1] = len(word1)-i
            
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]:
                    dp_cur[j] = dp_prev[j+1]
                else:
                    dp_cur[j] = min(
                        1+dp_prev[j],
                        1+dp_prev[j+1],
                        1+dp_cur[j+1],
                    )

            dp_prev = dp_cur.copy()
        return dp_prev[0]