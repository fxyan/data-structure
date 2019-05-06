"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
开心外排
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(0)
        res = head
        carry = 0
        while l1 and l2:
            res_val = l1.val + l2.val
            head.next = ListNode((res_val + carry) % 10)
            head = head.next
            carry = (res_val + carry) // 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            head.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            head = head.next
            l1 = l1.next
        while l2:
            head.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            head = head.next
            l2 = l2.next
        if carry > 0:
            head.next = ListNode(carry)
        return res.next