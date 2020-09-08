class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        maxElement = max(self.peekMax(), x)
        self.stack.append((x, maxElement))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        return self.stack.pop()[1]

    # Your MaxStack object will be instantiated and called as such:
    # obj = MaxStack()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.peekMax()
    # param_5 = obj.popMax()