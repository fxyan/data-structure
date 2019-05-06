"""
输入一个32位整数，输出该数二进制表示中1的个数。

注意：

负数在计算机中用其绝对值的补码来表示。
样例1
输入：9
输出：2
解释：9的二进制表示是1001，一共有2个1。
样例2
输入：-2
输出：31
解释：-2在计算机里会被表示成11111111111111111111111111111110，
      一共有31个1。

使用位运算 n = n&(n-1) 是削减最后一位1
负数 n &= 0xFFFFFFFF  可以得到对应的补码
"""


class Solution(object):
    def NumberOf1(self,n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        if n < 0:
            n &= 0xFFFFFFFF
        while n != 0:
            n = n & (n-1)
            res += 1
        return res
