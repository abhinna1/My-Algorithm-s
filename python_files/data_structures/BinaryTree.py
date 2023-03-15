class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def addNode(self, data) -> None:
        # If the graph is empty.
        if self.root == None:
            self.root = Node(data)
            return
        curr = self.root
        # next = self.curr.next
        while curr != None:
            if data > curr.data:
                if curr.right == None:
                    curr.right = Node(data)
                    break
                else:
                    curr = curr.right
                    # return
            else:
                if curr.left == None:
                    curr.left = Node(data)
                    break
                else:
                    curr = curr.left
                    # return
        
    def getRoot(self) -> Node:
        return self.root
    

bst = BinaryTree()

bst.addNode(10)
bst.addNode(11)
bst.addNode(2)
bst.addNode(4)

print(bst.getRoot().left.right.data)