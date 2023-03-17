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
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop())

stack.printStack()
