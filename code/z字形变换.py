"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

按照字符顺序输出  将第一行的字母放进列表的第一个元素 第二行放进第二个元素
"""


def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    这个是有规律的
    """
    reverse = False
    res = []
    index = 0
    if numRows <= 1:
        return s
    for i in range(numRows):
        res.append('')
    for i in range(len(s)):
        res[index] = s[i]
        if index == numRows - 1:
            reverse = True
        if index == 0:
            reverse = False
        index = index + 1 if reverse is False else index - 1
    return ''.join(res)
