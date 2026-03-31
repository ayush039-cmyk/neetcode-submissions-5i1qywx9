class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        for i in tokens:
            stack.append(i)
            if stack[-1] == "+":
                result = int(stack[-3]) + int(stack[-2])
                for i in range(3):
                    stack.pop()
                stack.append(result)
                result = 0
            elif stack[-1] == "-":
                result = int(stack[-3]) - int(stack[-2])
                for i in range(3):
                    stack.pop()
                stack.append(result)
                result = 0
            elif stack[-1] == "*":
                result = int(stack[-2]) * int(stack[-3])
                for i in range(3):
                    stack.pop()
                stack.append(result)
                result = 0
            elif stack[-1] == "/":
                result = int(int(stack[-3]) / int(stack[-2]))
                for i in range(3):
                    stack.pop()
                stack.append(result)
                result = 0
        return stack[0]      