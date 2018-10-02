class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.length = 0
        self.tailnode = None

    def __len__(self):
        return self.length

    # 在链表开头添加节点
    def prepend(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)
        node.next = self.root.next
        if self.tailnode is None:  # 判断尾节点是否为空为空则修改
            self.tailnode = node
        self.root.next = node
        self.length += 1

    def append(self, value):
        node = Node(value)
        tailnode = self.tailnode
        if tailnode is not None:  # 如果已有尾节点那么就在后面修改
            tailnode.next = node
        else:
            self.root.next = node  # 如果没有就直接在root后面指定
        self.tailnode = node
        self.length += 1

    # 删除最后一个元素
    def pop(self):
        tailnode = self.tailnode
        root = self.root
        if root.next == self.tailnode:  # 如果链表只有一个节点
            root.next = None
            value = tailnode.value
            self.tailnode = None
        else:
            while root.next is not tailnode:  # 循环遍历到倒数第二个节点
                root = root.next
            root.next = None
            value = tailnode.value
            self.tailnode = root
        self.length -= 1
        print(value)

    def popleft(self):
        if self.root.next is None:
            raise Exception('pop from empty LinkList')
        headnode = self.root.next
        if headnode == self.tailnode:
            self.tailnode = None
        self.root.next = headnode.next
        value = headnode.value
        del headnode
        self.length -= 1
        print(value)
        return value

    # 查找元素
    def find(self, value):
        index = 0
        for curnode in self.iter_node():
            if curnode.value == value:
                print(index)
                return index
            index += 1
        return -1

    def remove(self, value):  # O(n)
        prevnode = self.root
        """
        curnode = self.root.next
        这里是不需要迭代函数的删除
        while curnode is not None:
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode == self.tailnode:
                    self.tailnode = prevnode
                del curnode
                self.length -= 1
                return 1
            else:
                curnode = curnode.next
                prevnode = prevnode.next
        """
        for curnode in self.iter_node():  #循环遍历所有节点
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode == self.tailnode:
                    self.tailnode = prevnode  # 如果是尾节点就更改
                self.length -= 1
                return 1  # 删除成功就返回1
            else:
                prevnode = prevnode.next
        return -1  # 删除失败就返回-1

    def clear(self):
        for node in self.iter_node():
            del node
        self.tailnode = None
        self.root.next = None
        self.length = 0

    # 遍历链表
    def iter_node(self):
        curnode = self.root.next
        while curnode is not self.tailnode:  # 循环遍历除了尾节点的所有节点
            yield curnode
            curnode = curnode.next
        if curnode is not None:
            yield curnode

    def __iter__(self):
        for node in self.iter_node():  # 方便输出值
            yield node.value


def test_linked_list():
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)

    assert len(ll) == 4
    assert ll.find(2) == 2
    assert ll.find(-1) == -1

    assert ll.remove(0) == 1
    assert ll.remove(10) == -1
    assert ll.remove(2) == 1
    assert len(ll) == 2
    assert list(ll) == [1, 3]
    assert ll.find(0) == -1

    ll.prepend(0)
    assert list(ll) == [0, 1, 3]
    assert len(ll) == 3

    headvalue = ll.popleft()
    assert headvalue == 0
    assert len(ll) == 2
    assert list(ll) == [1, 3]

    assert ll.popleft() == 1
    assert list(ll) == [3]
    ll.popleft()
    assert len(ll) == 0
    assert ll.tailnode is None

    ll.clear()
    assert len(ll) == 0
    assert list(ll) == []


def test_linked_list_remove():
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.remove(7)
    print(list(ll))


def test_linked_list_append():
    ll = LinkedList()
    ll.prepend(1)
    ll.append(2)
    assert list(ll) == [1, 2]


if __name__ == '__main__':
    test_linked_list()
    test_linked_list_append()
    test_linked_list_remove()