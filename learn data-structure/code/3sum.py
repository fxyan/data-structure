"""
当时哔哩哔哩秋招的时候笔试大题就是这个，那个时候的我感觉没有抓住重点，沉迷于框架和网站，没有对基础进行
深入的学习，很悲惨的挂了，正好普林斯顿的算法课第一讲就是这个题
当时我写的是一个n三次方的暴力解法，不知道为什么一直不能oj
"""
import sys


def threesum(array, length, res):
    for i in range(length-2):
        k = length - 1
        j = i + 1
        while j < k:
            if array[i] + array[j] + array[k] == res:
                return [array[i], array[j], array[k]]
            elif array[i] + array[j] + array[k] < res:
                j += 1
            else:
                k -= 1
    return [-1, -1, -1]

if __name__ == "__main__":
    ans = []
    for i in range(2):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        ans.append(values)
    res = threesum(ans[1], ans[0][0], ans[0][1])
    print(res)
# if __name__ == "__main__":
#     # for line in sys.stdin:
#     #     a = line.split()
#     #     print(a)
#
#     # # 读取第一行的n
#     # n = int(sys.stdin.readline().strip())
#     # ans = 0
#     ans = []
#     for i in range(2):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         ans.append(values)
