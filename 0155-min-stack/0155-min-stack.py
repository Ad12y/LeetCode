class MinStack:

    def __init__(self):
        self.lst = []
        self.min_val = []
        

    def push(self, val: int) -> None:
        self.lst.append(val)
        if not len(self.min_val):
            self.min_val.append(val)
        else:
            self.min_val.append(min(self.min_val[-1], val))

    def pop(self) -> None:
        self.lst.pop()
        self.min_val.pop()
        
        
    def top(self) -> int:
        return self.lst[-1]
        
    def getMin(self) -> int:
        return self.min_val[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()