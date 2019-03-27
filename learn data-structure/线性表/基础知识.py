"""
线性表一般的操作
初始化一个空线性表
根据下标k返回一个相应的元素
在线性表中查找元素x的第一次出现的位置
在下标i之前插入一个新元素x
删除指定位序的元素
返回线性表l的长度n

"""
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class stack():
    def __init__(self):
        self.stack1 = Node()

    def is_empty(self):
        return self.stack1.next is None

    def pop(self):
        if not self.is_empty():
            node = self.stack1.next
            self.stack1.next = node.next
        print(node.val)
        return node

    def push(self, val):
        self.stack1.next = Node(val, self.stack1.next)


stack2 = stack()
stack2.push(1)
stack2.push(2)
stack2.push(3)
stack2.pop()
stack2.pop()
stack2.pop()