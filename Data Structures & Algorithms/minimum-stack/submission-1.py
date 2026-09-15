class MinStack:
    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, item):
        if not self.stack:
            self.stack.append(0)
            self.min = item
        else:
            self.stack.append(item - self.min)
            if item < self.min:
                self.min = item
        
    def pop(self):
        if not self.stack:
                return
        
        poppedElement = self.stack.pop()
        if poppedElement < 0:
            self.min = self.min - poppedElement

    def top(self):
        if not self.stack:
            return
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self):
        return self.min