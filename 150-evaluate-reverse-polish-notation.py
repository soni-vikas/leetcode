class Solution:
    operators = {
        "+": lambda x, y: int(x) + int(y), 
        "-": lambda x, y: int(x) - int(y), 
        "*": lambda x, y: int(x) * int(y), 
        "/": lambda x, y: int(x) / int(y),
    }

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in self.operators:
                y = stack.pop()
                x = stack.pop()
                stack.append(self.operators[t](x, y))

            else:
                stack.append(int(t))

        return int(stack[0])
