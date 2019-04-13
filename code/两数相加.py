"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

使用外排来进行操作 定义一个carry变量用来记录超过10的进位的数
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    主要使用了外排的手段处理
    """
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    carry = 0
    res = ListNode(None)
    p = res
    while l1 and l2:
        p.next = ListNode((l1.val + l2.val + carry) % 10)
        carry = (l1.val + l2.val + carry) // 10
        l1 = l1.next
        l2 = l2.next
        p = p.next
    while l1:
        p.next = ListNode((l1.val + carry) % 10)
        carry = (l1.val + carry) // 10
        p = p.next
        l1 = l1.next
    while l2:
        p.next = ListNode((l2.val + carry) % 10)
        carry = (l2.val + carry) // 10
        p = p.next
        l2 = l2.next
    if carry:
        p.next = ListNode(carry)
    return res.next
