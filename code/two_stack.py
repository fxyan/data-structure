class Stack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> None:
        return self.stack1.pop()


    def top(self) -> int:
        if len(self.stack1) != 0:
            return self.stack1[-1]

    def empty(self):
        if len(self.stack1) == 0:
            return True
        return False


# p = Stack()
# p.push(1)
# p.push(2)
# p.push(3)
# p.push(4)
# print(p.pop())
# p.push(3)
# p.push(4)
# print(p.pop())
# print(p.pop())
# print(p.pop())
# print(p.pop())
# print(p.pop())
