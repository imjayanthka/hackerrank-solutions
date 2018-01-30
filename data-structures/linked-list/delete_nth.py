def Delete(head, position):
    if position == 0:
        return head.next
    else:
        head.next = Delete(head.next, position - 1)
        
    return head