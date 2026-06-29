class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for t in tokens:
            if t == '+':
                r = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(r)
            elif t == '-':
                r = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(r)
            elif t == '*':
                r = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(r)
            elif t == '/':
                r = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(r)
            else:
                stack.append(int(t))


        return stack[-1]