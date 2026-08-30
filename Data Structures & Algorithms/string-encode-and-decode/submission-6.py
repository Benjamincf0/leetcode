class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        
        for s in strs:
            res.append(f"{len(s):3.0f}")
            res.append(s)

        out = ''.join(res)

        return out

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0

        while index < len(s):
            num = int(s[index: index+3])
            index += 3

            string = s[index: index+num]

            res.append(string)

            index += num

        return res