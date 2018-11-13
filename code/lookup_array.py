"""
二维数组查找数据
首先确定行数和列数
将左下角第一个数设为n
如果这个整数比n大,那么就排除这一行 向上查询
如果这个整数比n小,那么就排除这一列像右查询
"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array) - 1
        cols = len(array[0]) - 1
        i = rows
        j = 0
        while j <= cols and i >= 0:
            if array[i][j] > target:
                i -= 1
            elif array[i][j] < target:
                j += 1
            else:
                return True
        return False

"""

"""