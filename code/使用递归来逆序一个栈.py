from Stack import Stack


def getAndRemoveLastElement(stack):
    res = stack.pop()
    if stack.empty():
        return res
    else:
        last = getAndRemoveLastElement(stack)
        stack.push(res)
        return last


def reverse(stack):
    if stack.empty():
        return
    i = getAndRemoveLastElement(stack)
    # print(i, 1)
    reverse(stack)
    stack.push(i)


def test():
    stack1 = Stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    reverse(stack1)
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())


if __name__ == '__main__':
    test()