# https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1
# iterative soln
def reverseList(head):
    curr = head
    prev = None
    while(curr!=None):
        Next = curr.next
        curr.next = prev
        prev = curr
        curr = Next
    head = prev
    return head
# recursive soln:
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            newHead = head
            return newHead
        
        cur = self.reverseList(head.next) // pointing to New Head
        head.next.next = head
        head.next = None
        return cur

        

# https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1
def getCount(head_node):
    #code here
    count = 1
    cur = head_node
    while cur.next != None:
        count += 1
        cur= cur.next
    
    return count
    
def getNthfromEnd(head,n):
    #code here
    l = getCount(head)
    if n<0 or n>l:
        return -1
    else:
        cur = head
        if l-n > 0:
            for i in range(0, l-n):
                cur = cur.next
            return cur.data
        else:
            return cur.data

# https://practice.geeksforgeeks.org/problems/count-nodes-of-linked-list/1
def getCount(head_node):
    #code here
    count = 1
    cur = head_node
    while cur.next != None:
        count += 1
        cur= cur.next
    
    return count