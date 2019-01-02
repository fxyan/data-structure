"""
判断链表是否是回文结构的不用辅助空间的算法
if head is None or head.next is None:
            return True
        n1 = head
        n2 = head
        while n2.next is not None and n2.next.next is not None:
            n1 = n1.next
            n2 = n2.next.next
        n2 = n1.next
        n3 = None
        n1.next = None
        while n2 is not None:
            n3 = n2.next
            n2.next = n1
            n1 = n2
            n2 = n3
        n3 = n1
        n2 = head
        res = True
        while n1 is not None and n2 is not None:
            if n1.val != n2.val:
                res = False
                break
            n1 = n1.next
            n2 = n2.next
        n1 = n3.next
        n3.next = None
        while n1 is not None:
            n2 = n1.next
            n1.next = n3
            n1 = n2
            n3 = n1
        return res

"""
