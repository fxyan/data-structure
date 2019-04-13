"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

如果是负数直接返回false
定义一个reverse 为 0
while
先将reverse * 10 然后加上  对原来的数对10取余
原数 除 10 直到原数为0
"""


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    reverse = 0
    x1 = x
    while x1 > 0:
        reverse *= 10
        reverse += x1 % 10
        x1 = int(x1 / 10)
    if reverse == x:
        return True
    return False
