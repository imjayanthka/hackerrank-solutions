def Reverse(head):
    if head is None or head.next is None:
            return head
    else:
        if head.next is None:
            return head
        else:
            val = Reverse(head.next)
            head.next.next = head
            head.next = None
            return val