# 堆的实现


class Node(object):
    def __init__(self, element=None, next=None):
        self.element = element
        self.next = next

    def __repr__(self):
        return str(self.element)


class Stack(object):
    def __init__(self):
        self.head = Node()

    # 判断堆是不是空的
    def empty(self):
        return self.head.next is None

    # 增加一个Node 让self.head.next指向他但是让node的next指向当前的head.next 在这里是一个反向队列只能看到最后一个进来的
    def append(self, element):
        self.head.next = Node(element, self.head.next)

    # 如果head.next有值就删掉最后一个将栈中的前一个拿出来代替
    def pop(self):
        node = self.head.next
        if not self.empty():
            self.head.next = node.next
        return node


def test():
    ss = Stack()
    ss.append(1)
    ss.append(2)
    ss.append(3)
    ss.append(4)

    print(ss.pop())
    print(ss.pop())
    print(ss.pop())
    print(ss.pop())


if __name__ == '__main__':
    test()