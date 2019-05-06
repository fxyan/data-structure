"""
输入一个整数 n ，求斐波那契数列的第 n 项。

假定从0开始，第0项为0。(n<=39)

样例
输入整数 n=5

返回 5
"""


class Solution(object):
    def Fibonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = 1
        while n > 0:
            c = a + b
            a = b
            b = c
            n -= 1
        return a
