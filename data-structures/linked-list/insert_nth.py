def InsertNth(head, data, position):
    if head is None:
        return Node(data)
    else:
        if position == 0:
            head = Node(data, head)
        else:
            if head is None:
                return Node(data)
            else:
                head.next = InsertNth(head.next, data, position - 1)
    return head