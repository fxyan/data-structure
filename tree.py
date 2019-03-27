"""
满二叉树 就是所有节点就要满的，不能有空缺节点
完全二叉树 除了最后一层叶子结点要求不同其余和满二叉树一样， 叶子结点都是从左到右的中间不能有空缺
二叉搜索树 左子树都比他小 右子树都比他大  插入数据就是比较大小找到不能再找的位置然后然后插入
"""
import sys


def select_ball(k, n, nums):
    size = k - 1
    num = nums[size]
    while num != n:
        if num < n:


def deal_str(array, size, output):
    dict_num = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
                'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18,
                't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, '0': 26, '1': 27, '2': 28,
                '3': 29, '4': 30, '5': 31, '6': 32, '7': 33, '8': 34, '9': 35}
    array_num = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    out = ''
    if size == 1:
        for i in output:
            num = array[dict_num[i]]
            out = out + num
    elif size == 0:
        for i in output:
            num = array_num[array.index(i)]
            out = out+num
    return out





if __name__ == "__main__":
    # 读取第一行的n
    k, n = sys.stdin.readline().split()
    k = int(k)
    n = int(n)
    print('n', k, n)
    array = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().split()
        array.append(int(line[0]))
    print(array)

    # array = sys.stdin.readline().split()
    # size = sys.stdin.readline().split()
    # output = sys.stdin.readline().split()
    # array = [i for i in str(array[0])]
    # size = int(size[0])
    # output = str(output[0])
    # print(deal_str(array, size, output))



