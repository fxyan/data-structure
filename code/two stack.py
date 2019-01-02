class Stack(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        # if len(self.stack1) == 0:
        #     return 1
        # 边界条件保证多次push也不会打乱顺序
        if len(self.stack2) > 0:
            return self.stack2.pop()
        # 主体
        while len(self.stack1) != 0:
            node = self.stack1.pop()
            self.stack2.append(node)
        if len(self.stack2) != 0:
            return self.stack2.pop()
        return None


p = Stack()
p.push(1)
p.push(2)
p.push(3)
p.push(4)
print(p.pop())
p.push(3)
p.push(4)
print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())
