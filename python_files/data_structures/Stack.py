class Stack:
    def __init__(self):
        self.stack = []
        self.head = None
        
    def push(self, data) -> None:
        self.stack.append(data)
    
    def pop(self) -> int:
        return self.stack.pop()
    
    def printStack(self) -> None:
        print(self.stack)