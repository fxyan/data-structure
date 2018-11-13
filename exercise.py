"""
一个定长的列表首先你要确定列表的长度
"""

# class Array(object):
#     def __init__(self, size):
#         self.size = size
#         self._item = [None] * self.size
#
#     def __len__(self):
#         return len(self._item)
#
#     def __getitem__(self, item):
#         return self._item[item]
#
#     def __setitem__(self, key, value):
#         self._item[key] = value
#
#     def clear(self):
#         for i in range(len(self._item)):
#             self._item[i] = None
#
#     def __iter__(self):
#         for item in self._item:
#             yield item
#
#     def __repr__(self):
#         return '{}'.format(self._item)


# xx = Array(maxsize=8)
# xx[0] = 9
# xx[1] = 3
# print(xx)
# xx.clear()
# print(xx)

"""
冒泡排序
    首先从第一个数循环到倒数第二个数 n-1  最后一个数已经被安排了
    内层循环开始从第一个数开始循环 n-1-i次,因为i也被安排了
    边界检测如果为没有数
"""


def bubble_sort(seq):
    for i in range(len(seq) - 1):
        for j in range(len(seq) - 1 - i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    return seq


"""
选择排序 就是直接定义第一个数是最小值，然后开始循环找到真正最小值的坐标然后两个交换
不需要检查最后一个因为最后一个会在自动排序完成
"""


def select_sort(seq):
    for i in range(len(seq) - 1):
        min_size = i
        for j in range(i + 1, len(seq)):
            if seq[min_size] > seq[j]:
                min_size = j
        if min_size != i:
            seq[i], seq[min_size] = seq[min_size], seq[i]
    return seq


"""
插入排序
    将一个数据插入到已经排好序的数组中
    判断他的值是不是最小的如果不是就一直前移
"""


def insert_sort(seq):
    n = len(seq)
    for i in range(1, n):
        value = seq[i]
        pos = i
        while pos > 0 and value < seq[pos - 1]:
            seq[pos] = seq[pos - 1]
            pos -= 1
        seq[pos] = value
    return seq


"""
快排 使用了递归的排序
基本思路就是找到一个中间点,然后将自己的数组分成两部分左部分右部分和中间点,然后递归回去

"""


def quick_sort(seq):
    if len(seq) < 2:
        return seq
    else:
        pivot_index = 0
        pivot_value = seq[pivot_index]
        less_part = [i for i in seq[pivot_index + 1:] if i <= pivot_value]
        greed_part = [i for i in seq[pivot_index + 1:] if i > pivot_value]
        return quick_sort(less_part) + [pivot_value] + quick_sort(greed_part)


# seq = [1, 3, 2, 6, 0, 6, 3, 7, 9, 4]
# aa = []
# # print(bubble_sort(aa))
# # print(select_sort(seq))
# # print(insert_sort(seq))
# print(quick_sort(seq))
# str = input()
# list_str = str.split(',')
# list_str[0] = list_str[0].split(' ')
# n = int(list_str[1])
# seq = [int(i) for i in list_str[0]]
# print(n, seq)
# seq = [int(i) for i in list_str1[0]]
# print(n, seq)
# print(list_str)
"""
判断数组中有没有三个数相加等于 你输入的整数
"""


# 三重循环的辣鸡写法
def equal1(seq, n):
    if len(seq) < 3:
        return False
    for i in range(len(seq) - 2):
        for j in range(i + 1, len(seq) - 1):
            for x in range(j + 1, len(seq)):
                print(x)
                if seq[i] + seq[j] + seq[x] == n:
                    return True
    return False


# 通过指针优化的写法
def equal(seq, n):
    if len(seq) < 3:
        return False
    for i in range(len(seq) - 2):
        j = i + 1
        k = len(seq) - 1
        while j != k:
            if seq[i] + seq[j] + seq[k] < n:
                j += 1
            elif seq[i] + seq[j] + seq[k] > n:
                n -= 1
            elif seq[i] + seq[j] + seq[k] == n:
                return True
    return False

# print(equal([1, 2, 3, 4, 6, 8, 9, 21, 56, 90], 168))


"""
单链表
需要root节点 
tailNode节点
len长度

函数
append right
append left
pop left
pop right
remove 
find
clear
iter node
"""

"""
class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkList(object):
    def __init__(self):
        self.root = Node()
        self.tailnode = None
        self.lenght = 0

    def __len__(self):
        return self.lenght

    def append(self, value):
        node = Node(value)
        tailnode = self.tailnode
        if tailnode is not None:
            tailnode.next = node
        else:
            self.root.next = node
        self.tailnode = node
        self.lenght += 1

    def prepend(self, value):
        root = self.root
        tailnode = self.tailnode
        node = Node(value)
        node.next = root.next
        if tailnode is None:
            self.tailnode = node
        root.next = node
        self.lenght += 1

    def pop(self):
        if self.root.next is None:
            raise Exception('pop from empty LinkList')
        root = self.root
        tailnode = self.tailnode
        if root.next == tailnode:
            root.next = None
            value = tailnode.value
            tailnode = None
        else:
            while root.next != tailnode:
                root = root.next
            root.next = None
            value = tailnode.value
            tailnode = root
        self.lenght -= 1
        print(value)

    def popleft(self):
        if self.root.next is None:
            raise Exception('pop from empty LinkList')
        root = self.root
        headnode = root.next
        tailnode = self.tailnode
        if headnode == tailnode:
            self.tailnode = None
        root.next = headnode.next
        value = headnode.value
        del headnode
        self.lenght -= 1
        # print(value)
        return value

    def remove(self, value):
        root = self.root
        current = self.root.next
        tailnode = self.tailnode
        while current is not None:
            if current.value == value:
                root.next = current.next
                if current == tailnode:
                    self.tailnode = root
                del current
                self.lenght -= 1
                return 1
            else:
                root = root.next
                current = current.next
        return -1

    def find(self, value):
        if self.root.next is None:
            raise Exception('find from empty LinkList')
        current = self.root.next
        index = 0
        while current is not None:
            if current.value == value:
                return index
            else:
                current = current.next
                index += 1
        return -1

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.tailnode = None
        self.lenght = 0

    def iter_node(self):
        current = self.root.next
        tailnode = self.tailnode
        while current is not tailnode:
            yield current
            current = current.next
        if current is not None:
            yield current

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

def test_linked_list():
    ll = LinkList()

    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    # for i in ll:
    #     print('2', i)

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
    # print('tailnode', ll.tailnode.value)
    assert ll.tailnode is None

    ll.clear()
    assert len(ll) == 0
    assert list(ll) == []



def test_linked_list_remove():
    ll = LinkList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    print(list(ll))
    ll.remove(7)
    print(list(ll))


def test_linked_list_append():
    ll = LinkList()
    ll.prepend(1)
    ll.append(2)
    assert list(ll) == [1, 2]



def printListFromTailToHead(listNode):
    # write code here
    if listNode.value is not None:
        val = listNode.value
        listNode = listNode.next
    else:
        return []
    return printListFromTailToHead(listNode) + [val]

# if __name__ == '__main__':
#     # test_linked_list()
#     # test_linked_list_append()
#     # test_linked_list_remove()
#     ll = LinkList()
#     ll.append(3)
#     ll.append(4)
#     ll.append(5)
#     ll.append(6)
#     ll.append(7)
#     print(list(ll))
#     # printListFromTailToHead(ll)

ll = LinkList()
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append(7)


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        code = []
        head = listNode
        while head:
            code.insert(0, head.val)
            head = head.next
        return code
"""

"""
双端链表
"""
# class Node(object)
#     def __init__(self, value=None, next=None, ):

"""
哈希函数
"""


class HashTable(object):
    def __init__(self):
        self.table_size = 20007
        self.table = [0] * self.table_size

    def _index(self, key):
        return self._hash(key) % self.table_size

    def _hash(self, key):
        i = 0
        f = 1
        for j in key:
            i += ord(j) * f
            f *= 10
        return i

    def _insert_at_index(self, index, key, value):
        data = [key, value]
        v = self.table[index]
        if isinstance(v, int):
            self.table[index] = [data]
        else:
            self.table[index].append(data)

    def add(self, key, value):
        index = self._index(key)
        self._insert_at_index(index, key, value)

    def get(self, key, default=None):
        index = self._index(key)
        v = self.table[index]
        if isinstance(v, list):
            for kv in v:
                if kv[0] == key:
                    return kv[1]
        else:
            return default

    def has_key(self, key):
        index = self._index(key)
        v = self.table_size[index]
        for kv in v:
            if kv[0] == key:
                return True
        return False


def test():
    import uuid
    names = [
        'liu',
        'trtre',
        'name',
        'web',
        'python',
    ]
    ht = HashTable()
    for key in names:
        value = uuid.uuid4()
        ht.add(key, value)
        print('add 元素', key, value)
    for key in names:
        v = ht.get(key)
        print('get 元素', key, v)
    # ht.items()
    # for i in ht.values():
    #     print(i)
    # ht['wang'] = 23333
    # print(ht['wang'])


class Node(object):
    def __init__(self, element=None, next=None):
        self.element = element
        self.next = next

    def __repr__(self):
        return str(self.element)


class Stack(object):
    def __init__(self):
        self.head = Node()

    def empty(self):
        return self.head.next is None

    def append(self, element):
        self.head.next = Node(element, self.head.next)

    def pop(self):
        node = self.head.next
        if not self.empty():
            self.head.next = node.next
        return node

    def top(self):
        return self.head.next


# if __name__ == '__main__':
#     test()



