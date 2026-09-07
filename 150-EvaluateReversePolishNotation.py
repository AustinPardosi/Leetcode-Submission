class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if len(stack)>1 and token in {"+", "-", "*", "/"}:
                val2 = stack.pop()
                val1 = stack.pop()
                if token == '+':
                    newVal = val1 + val2
                elif token == '-':
                    newVal = val1 - val2
                elif token == '*':
                    newVal = val1 * val2
                else:
                    newVal = val1 / val2
                stack.append(int(newVal))
            else:
                stack.append(int(token))
            
        return stack[0]