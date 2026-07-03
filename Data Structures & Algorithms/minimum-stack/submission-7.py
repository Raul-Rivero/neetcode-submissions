class MinStack:

    def __init__(self):
        self.MainStack = []
        self.MinStack = []

    def push(self, val: int) -> None:
        self.MainStack.append(val)
        if self.MinStack:
            val = min(val, self.MinStack[-1])
        self.MinStack.append(val)

        # print(self.MainStack)
        print(self.MinStack)

    def pop(self) -> None:
        self.MainStack.pop()
        self.MinStack.pop()

    def top(self) -> int:
        return self.MainStack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]
