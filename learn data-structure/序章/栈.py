"""
你可以使用栈来模拟计算机的加减乘除操作
具体思路 首先你需要两个栈
一个栈装具体的数字
一个栈装运算符
忽略左括号将数字压入第一个栈中 将运算符压入第二个栈中 当你遇到右括号的时候将运算符栈弹出一个运算符，然后数字栈
弹出两个字符进行计算直到运行结束得到结果

"""
# 下面我建立一个定长的栈
class Stack():
    def __init__(self, size):
        self.size = size
        self.len = 0
        self.array = []

    def push(self, val):
        if self.len < self.size:
            self.array.append(val)
            self.len += 1
        else:
            print('该栈已经达到了最大值{}'.format(self.size))

    def pop(self):
        if self.len > 0:
            val = self.array.pop()
            self.len -= 1
            print(val)
            return val
        print('该栈已经没有值可以pop了')

    def isEmpty(self):
        if self.len > 0:
            return False
        return True

    def __iter__(self):
        return self

    def __next__(self):
        x = self.len - 1
        while x >= 0:
            print(self.array[x])
            x -= 1
        raise StopIteration


if __name__ == '__main__':
    c = Stack(4)
    c.push('诺诺')
    c.push('子航')
    c.push('凯撒')
    c.push('明妃')
    for i in c:
        print(i)
    c.pop()
    print(c.isEmpty())
    c.pop()
    c.pop()
    c.pop()
    print(c.isEmpty())
