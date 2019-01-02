"""
固定数组实现队列和栈
"""


class Stack(object):
    def __init__(self, size):
        self.index = 0
        self.size = size
        self.stack = []

    def push(self, value):
        if self.index == self.size:
            raise BaseException('栈已满')
        else:
            self.stack.append(value)
            self.index += 1

    def pop(self):
        if self.index == 0:
            raise ('栈中无元素')
        else:
            x = self.stack.pop()
            self.index -= 1
            return x

    def peek(self):
        if self.index > 0:
            return self.stack[self.index - 1]

    def is_empty(self):
        if self.index <= 0:
            return True
        else:
            return False


def test1():
    x = Stack(3)
    x.push(1)
    x.push(2)
    x.push(3)
    # x.push(4)
    print(x.pop())
    print(x.pop())


"""
固定数组实现队列
"""


class queue(object):
    def __init__(self, size):
        self.size = size
        self.start = 0
        self.end = 0
        self.len = 0
        self.queue = [None] * self.size

    def is_empty(self):
        if self.len <= 0:
            return True
        else:
            return False

    def push(self, value):
        if self.len > self.size:
            raise BaseException('队列已满')
        else:
            self.queue[self.end] = value
            self.end = 0 if self.end + 1 == self.size else self.end + 1
            self.len += 1

    def pop(self):
        if self.len > 0:
            x = self.queue[self.start]
            self.start = 0 if self.start + 1 == self.size else self.start + 1
            self.len -= 1
            return x
        else:
            raise BaseException('队列中无数字')


def test2():
    x = queue(3)
    x.push(1)
    x.push(2)
    # print(x.is_empty())
    x.push(3)
    # x.push(4)
    print(x.pop())
    print(x.pop())


"""
实现一个特殊的栈实现一个返回当前栈中最小元素的函数，要求时间复杂度为O(1)
"""


class Stack2(object):
    def __init__(self, stack1, stack2, size):
        self.data = stack1(size)
        self.min = stack2(size)

    def push(self, value):
        if self.min.is_empty():
            self.min.push(value)
        elif value < self.get_min():
            self.min.push(value)
        else:
            value = self.min.peek()
            self.min.push(value)
        self.data.push(value)

    def pop(self):
        if self.data.is_empty():
            return None
        else:
            self.min.pop()
            return self.data.pop()

    def get_min(self):
        if self.min.is_empty():
            return None
        return self.min.peek()


def test3():
    stack = Stack2(Stack, Stack, 3)
    stack.push(1)
    stack.push(2)
    stack.get_min()
    print(stack.pop())


"""
两个队列实现一个栈
"""


class TwoQueueStack(object):
    def __init__(self, queue1, queue2):
        self.data = queue1
        self.help = queue2

    def push(self, value):
        self.data.push(value)

    def pop(self):
        while self.data.len > 1:
            self.help.push(self.data.pop())
        res = self.data.pop()
        self.data, self.help = self.help, self.data
        return res


def test4():
    xx = TwoQueueStack(queue(3), queue(3))
    xx.push(1)
    xx.push(2)
    print(xx.pop())
    print(xx.pop())


"""
两个栈实现队列
"""


class TwoSteakQueue():
    def __init__(self, steak1, steak2):
        self.data = Stack(steak1)
        self.help = Stack(steak2)

    def push(self, value):
        self.data.push(value)

    def pop(self):
        while self.help.index > 0:
            return self.help.pop()
        while self.data.index > 0:
            self.help.push(self.data.pop())
        return self.help.pop()


def test_twoqueue():
    queue = TwoSteakQueue(3, 3)
    queue.push(3)
    queue.push(2)
    queue.push(1)
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())

if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    test_twoqueue()