class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            mx = self.stack[-1][1]
            self.stack.append((x, max(x, mx)))

    def pop(self) -> int:
        if self.stack:
            e = self.stack.pop()
            return e[0]
        return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return None

    def peekMax(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return None

    def popMax(self) -> int:
        top = self.stack.pop()

        temp = []
        while top[0] != top[1]:
            temp.append(top[0])
            top = self.stack.pop()

        for e in temp[::-1]:
            # use self.push to store ele again with max calculated
            self.push(e)

        return top[0]