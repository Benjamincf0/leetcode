class Solution:
    sep = "peeenis"

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        return self.sep.join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0: return [""]
        return s.split(self.sep)