def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    q = None
    while head is not None:
        p = head
        head = head.next
        p.next = q
        q = p
    return q
