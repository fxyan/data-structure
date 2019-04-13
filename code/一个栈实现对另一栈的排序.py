from two_stack import Stack


def sortStackByStack(stack):
    help = Stack()
    while not stack.empty():
        cur = stack.pop()
        while not help.empty() and cur > help.top():
            stack.push(help.pop())
        help.push(cur)
    while not help.empty():
        stack.push(help.pop())
    return stack


def test():
    stack1 = Stack()
    stack1.push(1)
    stack1.push(8)
    stack1.push(3)
    sortStackByStack(stack1)
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())


if __name__ == '__main__':
    test()
