class Node:
  def __init__(self, data):
    self.data=data
    self.next=None
  
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def addNode(self, data):
    if self.head == None:
      self.head = self.tail = Node(data)
      return
    # else
    new_node = Node(data)
    self.tail.next = new_node
    self.tail = self.tail.next
  def getData(self):
    curr = self.head
    if curr!=None:
      while curr != None:
        print(curr.data)
        curr = curr.next