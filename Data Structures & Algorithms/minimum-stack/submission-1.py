class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = None
        self.minPosTracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum == None:
            self.minimum = val
            self.minPosTracker.append(0)
        else:
            if val < self.minimum:
                self.minPosTracker.append(len(self.stack) - 1)
                self.minimum = val

    def pop(self) -> None:
        if self.minPosTracker[-1] == len(self.stack) - 1:
            self.minPosTracker.pop()
            #if it's empty
            if len(self.minPosTracker) == 0:
                self.minimum = None
            else:
                self.minimum = self.stack[self.minPosTracker[-1]]
        self.stack.pop() 

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minimum
