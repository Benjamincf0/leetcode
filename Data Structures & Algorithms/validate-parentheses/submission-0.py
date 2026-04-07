class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        c = {'}':'{', ')':'(', ']':'['}
        for letta in s[1:]:
            if letta not in c: stack.append(letta)
            elif letta in c:
                if len(stack)>0 and stack[-1] == c[letta]: stack.pop()
                else: return False
        return len(stack) == 0