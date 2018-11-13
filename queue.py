class Node(object):
    def __init__(self, element=None, next=None):
        self.element = element
        self.next = next

    def __repr__(self):
        return str(self.element)


class Queue(object):
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def empty(self):
        return self.head.next is None

    def append(self, element):
        node = Node(element)
        self.tail.next = node
        self.tail = node

    def pop(self):
        node = self.head.next
        if not self.empty():
            self.head = self.head.next
        return node


def test():
    q = Queue()

    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())


if __name__ == '__main__':
    test()
