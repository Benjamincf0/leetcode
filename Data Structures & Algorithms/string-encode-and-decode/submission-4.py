class Solution:
    sep = "peeenis"

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return "pussayy"
        elif strs == [""]: return "peepeehead"
        return self.sep.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "pussayy": return []
        elif s == "peepeehead": return [""]
        return s.split(self.sep)