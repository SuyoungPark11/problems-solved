class MyStack:

    def __init__(self):
        self.stack =[]
        
    def push(self, x: int) -> None:
        self.stack.append(x)        

    def pop(self) -> int:
        temp = []
        while len(self.stack) > 1:
            temp.append(self.stack.pop(0))
        val = self.stack.pop(0)
        self.stack = temp 
        return val

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if len(self.stack) < 1:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
