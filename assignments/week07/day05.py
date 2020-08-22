# https://practice.geeksforgeeks.org/problems/delete-keys-in-a-linked-list/1
def deleteAllOccurances(head, k):
    # return if list is empty
    if head == None:
        return
    
    #prev to keep track of previous node..  
    cur = head
    prev = None
    
    # If head and new heads after that contains the key
    while cur != None and cur.data == k:
        cur = head.next
        head = cur
    
    # to find the key in rest of the list
    while cur:
        while cur!= None and cur.data != k:
            prev = cur
            cur = cur.next

        # if key is not found then return the head(i.e do nothing)
        if cur == None:
            return head
        
        # if key is found, prev.next = cur.next would unlink the key
        prev.next = cur.next
        cur = cur.next

    return head



# https://practice.geeksforgeeks.org/problems/sum-of-binary-tree/1
def sumBT(root):
    if root == None:
        return 0
    return sumBT(root.left)+sumBT(root.right)+root.data