"""
冒泡排序
    首先从第一个数循环到倒数第二个数 n-1  最后一个数已经被安排了
    内层循环开始从第一个数开始循环 n-1-i次,因为i也被安排了
    边界检测如果为没有数



def bubble_sort(array):
    if array is None or len(array) < 2:
        return array
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


def test_bubble():
    array = [4, 2, 1, 7, 5, 3, 2, 4]
    array2 = [4, 4, 1]
    bubble_sort(array)
    bubble_sort(array2)
    print(array)
    print(array2)
"""

"""
选择排序 就是直接定义第一个数是最小值，然后开始循环找到真正最小值的坐标然后两个交换
不需要检查最后一个因为最后一个会在自动排序完成



def select_sort(array):
    if array is None or len(array) < 2:
        return array
    for i in range(len(array)-1):
        index = i
        for j in range(i+1, len(array)):
            if array[index] > array[j]:
                index = j
        if index != i:
            array[i], array[index] = array[index], array[i]


def test_select():
    array = [4, 2, 1, 7, 5, 3, 2, 4]
    array2 = [4, 4, 1]
    select_sort(array)
    select_sort(array2)
    print(array)
    print(array2)
"""

"""
插入排序
    将一个数据插入到已经排好序的数组中
    判断他的值是不是最小的如果不是就一直前移


def insert_sort(array):
    for i in range(1, len(array)):
        index = i
        value = array[i]
        while index > 0 and value < array[index-1]:
            array[index] = array[index-1]
            index -= 1
        if index != i:
            array[index] = value


def test_insert():
    array = [4, 2, 1, 7, 5, 3, 2, 4]
    array2 = [4, 4, 1]
    insert_sort(array)
    insert_sort(array2)
    print(array)
    print(array2)
"""

"""
快排 使用了递归的排序
基本思路就是找到一个中间点,然后将自己的数组分成两部分左部分右部分和中间点,然后递归回去


import random
def quick_sort(array):
    if len(array) < 2 or array is None:
        return array
    return quick(array, 0, len(array)-1)


def quick(array, l, r):
    if l < r:
        ran = random.randint(l, r)
        print(l, r)
        print(ran)
        array[ran], array[r] = array[r], array[ran]
        q = partition(array, l, r)
        print(q)
        quick(array, l, q[0])
        quick(array, q[1], r)


def partition(array, l, r):
    left = l-1
    right = r
    while l < right:
        if array[l] < array[r]:
            left += 1
            array[left], array[l] = array[l], array[left]
            l += 1
        elif array[l] > array[r]:
            right -= 1
            array[l], array[right] = array[right], array[l]
        else:
            l += 1
    array[r], array[l] = array[l], array[r]
    q = [left, right+1]
    return q


def test_quick():
    array = [4, 2, 1, 7, 5, 3, 2, 4]
    array2 = [4, 4, 1]
    quick_sort(array)
    quick_sort(array2)
    print(array)
    print(array2)

"""

"""
归并排序



def merge_sort(array):
    if len(array) < 2 or array is None:
        return array
    return sort_process(array, 0, len(array)-1)


def sort_process(array, l, r):
    if l == r:
        return None
    else:
        mid = (l+r)//2
        sort_process(array, l, mid)
        sort_process(array, mid+1, r)
        merge(array, l, mid, r)


def merge(array, l, mid, r):
    help = []
    left = l
    right = mid+1
    while left <= mid and right <= r:
        if array[left] < array[right]:
            help.append(array[left])
            left += 1
        else:
            help.append(array[right])
            right += 1
    while left <= mid:
        help.append(array[left])
        left += 1
    while right <= r:
        help.append(array[right])
        right += 1
    for i in range(len(help)):
        array[l+i] = help[i]


def test_merge():
    array = [4, 2, 1, 7, 5, 3, 2, 4]
    array2 = [4, 4, 1]
    merge_sort(array)
    merge_sort(array2)
    print(array)
    print(array2)
"""

"""
堆排序


def heap_sort(array):
    if len(array) < 2 or array is None:
        return array
    size = len(array)
    build_max(array, size)
    for i in range(size-1, -1, -1):
        array[i], array[0] = array[0], array[i]
        heap_insert(array, 0, i)


def build_max(array, size):
    for i in range((size-2)//2, -1, -1):
        heap_insert(array, i, size)


def heap_insert(array, root, size):
    left = root * 2 + 1
    while left < size:
        largest = left+1 if left+1 < size and array[left+1] > array[left] else left
        if array[root] < array[largest]:
            array[root], array[largest] = array[largest], array[root]
            root = largest
            left = root * 2 + 1
        else:
            return


def test_heap():
    array = [4, 2, 1, 7, 5, 3, 2, 4]
    array2 = [4, 4, 1]
    heap_sort(array)
    heap_sort(array2)
    print(array)
    print(array2)
"""

"""
判断数组中有没有三个数相加等于 你输入的整数



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
                k -= 1
            elif seq[i] + seq[j] + seq[k] == n:
                return True
    return False
"""

"""
判断排序之后数组的相邻的最大差值，使用非比较排序 时间复杂度为O(N)
def maxgap(array):
    if len(array) < 2 or array is None:
        return array
    smax = max(array)
    smin = min(array)
    if smax == smin:
        return 0
    size = len(array)
    min_size = [None] * (size + 1)
    max_size = [None] * (size + 1)
    bool_size = [False] * (size + 1)
    for i in range(len(array)):
        bid = backsize(array[i], size, smax, smin)
        max_size[bid] = array[i] if max_size[bid] is None or max_size[bid] < array[i] else max_size[bid]
        min_size[bid] = array[i] if min_size[bid] is None or min_size[bid] > array[i] else min_size[bid]
        bool_size[bid] = True
    res = 0
    print(min_size, max_size)
    lastmax = max_size[0]
    for i in range(len(min_size)):
        if bool_size[i]:
            res = max(res, max_size[i] - lastmax)
            lastmax = max_size[i]
    return res


def backsize(num, size, smax, smin):
    return (num - smin) * size // (smax - smin)


def test_max():
    array = [4, 2, 1, 7, 5, 3, 2, 4, 17]
    array2 = [4, 4, 1]
    print(maxgap(array))
    print(maxgap(array2))
"""

"""
数组结构实现大小固定的队列和栈



class Stack(object):
    def __init__(self, size):
        self.stack = [None] * size
        self.size = size
        self.len = 0

    def push(self, value):
        if self.len >= self.size:
            print('栈已经满了')
        else:
            self.stack[self.len] = value
            self.len += 1

    def get_min(self):
        if self.len == 0:
            return None
        return self.stack[self.len-1]

    def pop(self):
        if self.len < 0:
            print('无数据可以出栈')
        else:
            self.len -= 1
            value = self.stack[self.len]
            # print(value)
            return value


def test_stack():
    stack = Stack(3)
    stack.push(7)
    stack.push(8)
    stack.push(6)
    stack.push(77)
    stack.pop()
    stack.pop()
    stack.pop()


class Queue(object):
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.end = 0
        self.start = 0
        self.index = 0

    def push(self, value):
        if self.index < self.size:
            print(self.index)
            self.queue[self.end] = value
            self.end = 0 if self.end + 1 == self.size else self.end + 1
            self.index += 1
        else:
            print('队列已满')

    def pop(self):
        if self.index > 0:
            print(self.queue[self.start])
            self.start = 0 if self.start + 1 == self.size else self.start + 1
            self.index -= 1
        else:
            print('队列无数据')


def test_queue():
    queue = Queue(3)
    queue.push(5)
    queue.push(4)
    queue.push(3)
    queue.push(2)
    queue.pop()
    queue.pop()
    queue.pop()
    queue.pop()


class Steak2():
    def __init__(self, size):
        self.stack3 = Stack(size)
        self.stack4 = Stack(size)

    def push(self, value):
        self.stack3.push(value)
        if self.stack3.get_min() is None or value < self.stack3.get_min() :
            self.stack4.push(value)
        else:
            self.stack4.push(self.stack3.get_min())

    def pop(self):
        self.stack4.pop()
        return self.stack3.pop()

    def get_min(self):
        return self.stack4.get_min()

def test_steak2():
    steak = Steak2(3)
    steak.push(5)
    steak.push(4)
    steak.push(3)
    steak.pop()
    steak.pop()
    print(steak.get_min())
"""

"""
矩阵转圈打印

def order_print(array):
    tR = 0
    tC = 0
    dR = len(array) - 1
    dC = len(array[0]) - 1
    while tR <= dR and tC <= dC:
        print_edge(array, tR, tC, dR, dC)
        tR += 1
        tC += 1
        dR -= 1
        dC -= 1


def print_edge(array, tR, tC, dR, dC):
    if tC == dC:
        while tR <= dR:
            print(array[tR][tC], end=' ')
            tR += 1
    elif tR == dR:
        while tC <= dC:
            print(array[tR][tC], end=' ')
            tC += 1
    else:
        curR = tR
        curC = tC
        while tC < dC:
            print(array[tR][tC], end=' ')
            tC += 1
        while tR < dR:
            print(array[tR][tC], end=' ')
            tR += 1
        while dC > curC:
            print(array[dR][dC], end=' ')
            dC -= 1
        while dR > curR:
            print(array[dR][dC], end=' ')
            dR -= 1
        while dC > curC:
            print(array[dR][dC], end=' ')
            dC -= 1


def test_order():
    array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    array2 = [[1, 2, 3, 4]]
    array3 = [[1], [2], [3]]
    # order_print(array)
    order_print(array2)
    order_print(array3)
"""

"""
将矩阵的数字转换90度
1 2     4 1
4 5     5 2

def rotate(array):
    tR = 0
    tC = 0
    dR = len(array) - 1
    dC = len(array[0]) - 1
    while tR < dR or tC < dC:
        rotate_edge(array, tR, tC, dR, dC)
        tR += 1
        tC += 1
        dR -= 1
        dC -= 1


def rotate_edge(array, tR, tC, dR, dC):
    size = dC - tC
    for i in range(size):
        time = array[tR][tC+i]
        print(i)
        array[tR][tC+i] = array[dR-i][tC]
        array[dR-i][tC] = array[dR][dC-i]
        array[dR][dC-i] = array[tR+i][dC]
        array[tR+i][dC] = time


def test_rotate():
    array = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
    rotate(array)
    print(array)
"""

"""
之字形打印矩阵
"""

def print_zhi(array):
    tR = 0
    tC = 0
    dR = 0
    dC = 0
    endR = len(array) - 1
    endC = len(array[0]) - 1
    bool_1 = True
    while tR <= endR and dC <= endC:
        print_level(array, tR, tC, dR, dC, bool_1)
        tR = 0 if tC < endC else tR + 1
        tC = tC + 1 if tC < endC else tC
        dC = 0 if dR < endR else dC + 1
        dR = dR + 1 if dR < endR else dR
        bool_1 = False if bool_1 is True else True


def print_level(array, tR, tC, dR, dC, bool_1):
    if bool_1 is True:
        while dR >= tR and dC <= tC:
            print(array[dR][dC])
            dR -= 1
            dC += 1
    else:
        while tR <= dR and tC >= dC:
            print(array[tR][tC])
            tR += 1
            tC -= 1


def test_level():
    array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print_zhi(array)


if __name__ == '__main__':
    # test_bubble()
    # test_select()
    # test_insert()
    # test_quick()
    # test_merge()
    # test_heap()
    # test_max()
    # test_stack()
    # test_queue()
    # test_steak2()
    # test_order()
    # test_rotate()
    test_level()