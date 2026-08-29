class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        
        ref = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        res = []

        current = []

        def dfs(i):
            if i == len(digits):
                res.append("".join(current))
                return

            digit = int(digits[i])
            # print(digit)

            # digit -= 2
            # digit *= 3

            # letters = [chr(index+ord('a')) for index in range(digit, digit+3)]
            letters = ref[digit]

            for letter in letters:
                current.append(letter)
                dfs(i+1)
                current.pop()

        dfs(0)

        return res