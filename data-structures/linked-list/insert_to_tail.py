"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

def Insert(head, data):
    if head is None:
        return Node(data)
    else: 
        if head.next is not None:
            Insert(head.next, data)
        else:
            head.next = Node(data)
    return head