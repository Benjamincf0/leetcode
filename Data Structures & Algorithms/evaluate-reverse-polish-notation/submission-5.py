class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+', '-', '*', '/'}
        for token in tokens:
            if token in operands: # we've got an operation on our hands
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
                        res = int(n1/n2)

                stack.append(res)
                print(f"{n1}{token}{n2} = {res}")
            else:
                stack.append(int(token))
        print(stack)
        return stack[0]