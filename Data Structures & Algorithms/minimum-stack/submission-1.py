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
            # minimum element up to that point.
            # Invariant: The top of min_stack is
            # the minimum element of the main stack
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

# Alternative approach: Single stack with encoded values and min

# Numbers
# [3 5 2]

# Encoded Stack
# [0 2 -1]
# 2
