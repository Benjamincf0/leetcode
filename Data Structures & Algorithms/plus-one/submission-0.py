class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits)-1, -1, -1):
            s = digits[i] + c
            c = s // 10
            s %= 10
            digits[i] = s
        if c > 0:
            return [c]+digits
        return digits