class Solution:
    sep = "peeenis"

    def encode(self, strs: List[str]) -> str:
        return self.sep.join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split(self.sep)