# 前面写一些简单的递归函数


# 正序递归0,1,2,3,4,5
def PrintInc(n):
    if n > 0:
        PrintInc(n - 1)
        print(n)
    else:
        print(n)


# 倒序递归0,1,2,3,4,5
def PrintRev(n):
    if n > 0:
        print(n)
        PrintRev(n - 1)


# 汉诺塔
def move(n, a, b, c):
    if n == 1:
        print(a, '->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


if __name__ == '__main__':
    # PrintInc(5)
    # PrintRev(5)
    move(3, 'A', 'B', 'C')
