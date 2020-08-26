class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
  
class Queue:

  def __init__(self):
    self.head = None
    self.tail = None    
  
  def isEmpty(self):
    if self.head == None:
      return True
    else:
      return False

  def enqueue(self, val):
    cur = Node(val)

    if self.tail == None:
      self.tail=self.head=cur
      print(self.tail.val)
      return
    
    self.tail.next = cur
    self.tail = cur
    print(self.tail.val)
    return 

  def dequeue(self):
    if self.isEmpty():
      print('stack is empty!')
      return
    else:
      cur = self.head
      self.head = cur.next
      print(cur.val)
      if self.head == None:
        self.tail = None    
      return 

# q = Queue()
# q.enqueue(10)
# q.dequeue()
# q.enqueue(12)
# q.enqueue(14)
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()


