class Solution:
    def checkValidString(self, s: str) -> bool:

        count_min = 0
        count_max = 0

        for i in range(len(s)-1,-1,-1):
            if s[i] == '(':
                count_min -= 1
                count_max -= 1
            elif s[i] == ')':
                count_min += 1
                count_max += 1
            else:
                count_min -= 1
                count_max += 1

            count_min = max(count_min, 0)
            if count_max < 0: return False

        return count_min<=0 and count_max >=0