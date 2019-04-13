"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
直接
"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    reverse = 0
    neg = 1
    if x == 0:
        return 0
    if x < 0:
        neg = -1
    
    if reverse > 2 ** 31 - 1 or reverse < -(2 ** 31):
        return 0