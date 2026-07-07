class MinStack:

    def __init__(self):
        self.stack = [] # Stack
        self.min_stack = [] # Prefix Minimum

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            # For each i in min_stack, it is the
            # minimum element at that point in time.
            prev_min = self.min_stack[-1]
            next_min = min(prev_min, val)
            self.min_stack.append(next_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
