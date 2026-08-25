class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(opened: int, closed: int):
            if opened == closed == n:
                return res.append("".join(stack))

            if opened < n:
                # we must only have n opened...
                stack.append('(')
                dfs(opened+1, closed)
                stack.pop()

            if opened > closed:
                # otherwise, there is nothing to close...
                stack.append(')')
                dfs(opened, closed+1)
                stack.pop()


        dfs(0, 0)

        return res