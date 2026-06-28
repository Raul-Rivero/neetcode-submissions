class MinStack:

    def __init__(self):
        self.stack = []
        self.MinStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.MinStack:
            val = min(self.MinStack[-1],val)
            self.MinStack.append(val)
        else:
            self.MinStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.MinStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.MinStack)
        return self.MinStack[-1]
