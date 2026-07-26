class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf') # greater than all

    def push(self, val: int) -> None:
        if not self.stack: #empty stack
            self.stack.append(0) # since we always want to append val - min
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        if pop < 0:
            self.min = self.min - pop
        

    def top(self) -> int:
        if not self.stack:
            return
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
        
