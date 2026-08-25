class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        current = []

        def dfs(paren: str):
            if paren == '(':
                stack.append(paren)
            elif paren == ')' and len(stack)>0 and stack.pop() == '(':
                pass
            else:
                return

            current.append(paren)

            if len(current) == n+n:
                if len(stack) == 0:
                    res.append("".join(current))
            else:
                dfs('(')
                dfs(')')

            if paren == '(':
                stack.pop()
            elif paren == ')':
                stack.append('(')
            current.pop()

        dfs("(")

        return res