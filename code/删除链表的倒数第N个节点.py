"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

解法 设置一个key，遍历链表每次k-1如果k>0那么说明没有要删除的节点
如果k <= 0 那么从新遍历链表每次k+1找到k=0的节点就是要删除的节点
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n: int):
        if head is None:
            return head
        k = n
        head_1 = head
        res = head
        while head_1:
            head_1 = head_1.next
            k -= 1
        if k > 0:
            return res
        if k == 0:
            return res.next
        while head:
            k += 1
            if k == 0:
                head.next = head.next.next
                break
            head = head.next
        return res