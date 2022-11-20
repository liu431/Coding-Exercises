class MinStack:

    def __init__(self):
        self.stack = []
        self.minele = []

    def push(self, val: int) -> None:
        if not self.minele or val <= self.minele[-1]:
            self.minele.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.minele[-1] == self.stack[-1]:
            self.minele.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minele[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
