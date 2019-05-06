"""
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留。

样例1
输入：1->2->3->3->4->4->5

输出：1->2->5
样例2
输入：1->1->1->2->3

输出：2->3

这个题是比较绕的，思路有些清奇
    首先先设定一个虚拟节点 None 将他的next连到头结点上去
    p永远是前一个节点 q是p的下一个节点
    while 如果让q等于p.next 直到q的值为一个新的节点的值
    然后拿 p的第二个节点对比如果相等那么p直接下移
    如果不等那么将p的next指向q
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplication(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        new_head = ListNode(0)
        p = new_head
        while p.next:
            q = p.next
            while q and q.val == p.next.val:
                q = q.next
            if p.next.next == q:
                p = p.next
            else:
                p.next = q
        return new_head.next
