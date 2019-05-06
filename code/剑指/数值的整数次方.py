"""
实现函数double Power(double base, int exponent)，求base的 exponent次方。

不得使用库函数，同时不需要考虑大数问题。

注意：

不会出现底数和指数同为0的情况
样例1
输入：10 ，2

输出：100
样例2
输入：10 ，-2

输出：0.01

题解
    主要处理负数，负数的情况下是 1/res
"""


class Solution(object):
    def Power(self, base, exponent):
        """
        :type base: float
        :type exponent: int
        :rtype: float
        """
        res = base
        n = 0
        if exponent == 0:
            return 1
        if exponent < 0:
            exponent = abs(exponent)
            n = 1
        while exponent > 1:
            res *= base
            exponent -= 1
        if n != 0:
            return 1/res
        return res
