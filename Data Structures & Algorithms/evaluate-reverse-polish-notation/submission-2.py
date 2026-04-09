class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # operands = {}
        for token in tokens:
            if token <= '100' and token >= '-100':
                stack.append(int(token))
            else: # we've got an operation on our hands
                n2=stack.pop()
                n1=stack.pop()
                match token:
                    case '+':
                        res = n1+n2
                    case '-':
                        res = n1-n2
                    case '*':
                        res = n1*n2
                    case '/':
                        res = n1//n2
                stack.append(res)
        return stack[0]