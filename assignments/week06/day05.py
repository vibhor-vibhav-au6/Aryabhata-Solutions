class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        current = self.head

        for _ in range(0, index):
            current = current.next

        return current.val

    def addAtHead(self, val: int):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be
        the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int):
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked
        list, the node will be appended to the end of linked list. If index is greater than the length, the node will not
        be inserted.
        """
        if index > self.size:
            return

        current = self.head
        new_node = ListNode(val)

        if index <= 0:
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        current = self.head

        if index == 0:
            self.head = current.next
        else:
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next

        self.size -= 1

ll = MyLinkedList()
ll.addAtIndex(0,4)

class Stack():
  def __init__(self):
    self.ll = MyLinkedList()

  def push(self, val):
    self.ll.addAtHead(val)
  
  def pop(self):
    cur = self.ll.head.val
    self.ll.deleteAtIndex(0)
    return cur

  def peek(self):
    return self.ll.head.val
  
  def isEmpty(self):
    if self.ll.size == 0:
      return True
    else:
      return False



# driver code
# s = Stack()
# # print (s.peek)
# s.push(10)
# # a = []

# print(s.peek())
# s.push(12)
# print (s.peek())

# s.pop()
# print (s.peek())
# print(s.isEmpty())


# alternate way:
# class Node: 
      
#     # Class to create nodes of linked list 
#     # constructor initializes node automatically 
#     def __init__(self,data): 
#         self.data = data 
#         self.next = None
      
# class Stack: 
      
#     # head is default NULL 
#     def __init__(self): 
#         self.head = None
      
#     # Checks if stack is empty 
#     def isempty(self): 
#         if self.head == None: 
#             return True
#         else: 
#             return False
      
#     # Method to add data to the stack 
#     # adds to the start of the stack 
#     def push(self,data): 
          
#         if self.head == None: 
#             self.head=Node(data) 
              
#         else: 
#             newnode = Node(data) 
#             newnode.next = self.head 
#             self.head = newnode 
      
#     # Remove element that is the current head (start of the stack) 
#     def pop(self): 
          
#         if self.isempty(): 
#             return None
              
#         else: 
#             # Removes the head node and makes  
#             #the preceeding one the new head 
#             poppednode = self.head 
#             self.head = self.head.next
#             poppednode.next = None
#             return poppednode.data 
      
#     # Returns the head node data 
#     def peek(self): 
          
#         if self.isempty(): 
#             return None
              
#         else: 
#             return self.head.data 
      
#     # Prints out the stack      
#     def display(self): 
          
#         iternode = self.head 
#         if self.isempty(): 
#             print("Stack Underflow") 
          
#         else: 
              
#             while(iternode != None): 
                  
#                 print(iternode.data,"->",end = " ") 
#                 iternode = iternode.next
#             return
          
# # Driver code 
# MyStack = Stack() 
  
# MyStack.push(11)  
# MyStack.push(22) 
# MyStack.push(33) 
# MyStack.push(44) 
  
# # Display stack elements  
# MyStack.display() 
  
# # Print top element of stack  
# print("\nTop element is ",MyStack.peek()) 
  
# # Delete top elements of stack  
# MyStack.pop() 
# MyStack.pop() 
  
# # Display stack elements 
# MyStack.display() 
  
# # Print top element of stack  
# print("\nTop element is ", MyStack.peek())  

    
        