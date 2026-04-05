class MinStack:

    def __init__(self):
        self.stack = []
        self.mn = math.inf

    def push(self, val: int) -> None:
        self.mn = min(self.mn, val)
        self.stack.append((val, self.mn))

    def pop(self) -> None:
        v, m = self.stack.pop()
        if self.stack:
            v, m = self.stack[-1]
            self.mn = m
        else:
            self.mn = math.inf

    def top(self) -> int:
        v, m = self.stack[-1]
        return v

    def getMin(self) -> int:
        v, m = self.stack[-1]
        return m
