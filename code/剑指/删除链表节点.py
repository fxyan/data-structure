"""
给定单向链表的一个节点指针，定义一个函数在O(1)时间删除该结点。

假设链表一定存在，并且该节点一定不是尾节点。

样例
输入：链表 1->4->6->8
      删掉节点：第2个节点即6（头节点为第0个节点）

输出：新链表 1->4->8

复制该节点下一个节点，然后代替本节点之后next.next
"""


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void
        """
        new_node = node.next
        node.val = new_node.val
        node.next = node.next.next