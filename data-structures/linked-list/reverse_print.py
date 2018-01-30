def ReversePrint(head):
    if head is None:
        return
    else:
        ReversePrint(head.next)
        print(head.data)