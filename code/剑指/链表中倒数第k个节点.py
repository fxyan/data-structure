"""
输入一个链表，输出该链表中倒数第k个结点。

注意：

k >= 0;
如果k大于链表长度，则返回 NULL;
样例
输入：链表：1->2->3->4->5 ，k=2

输出：4

先遍历链表每遍历一个节点k-=1
如果第一遍结束之后k依旧大于0那么返回None
否则第二遍遍历链表
每过一个节点k + 1 当k=0的时候返回节点
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def findKthToTail(self, pListHead, k):
        """
        :type pListHead: ListNode
        :type k: int
        :rtype: ListNode
        """
        head = pListHead
        while head is not None:
            k -= 1
            head = head.next
        if k > 0:
            return None
        while k != 0:
            k += 1
            pListHead = pListHead.next
        return pListHead