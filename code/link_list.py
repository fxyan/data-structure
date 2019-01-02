"""
判断链表是不是回文的
"""
# 第一种有辅助数组的
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        help = []
        link1 = head
        link2 = head
        while link1 is not None:
            help.append(link1.val)
            link1 = link1.next
        while link2 is not None:
            val = help.pop()
            if link2.val != val:
                return False
            link2 = link2.next
        return True



# 用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
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