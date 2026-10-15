class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]+=1

        for i in range(len(digits)-1, -1, -1):
            c, s = divmod(digits[i], 10)
            digits[i] = s

            if i > 0: digits[i-1] += c
            elif c > 0:
                digits = [c] + digits
                
        return digits