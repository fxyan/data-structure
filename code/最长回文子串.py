"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000
Manacher算法
pr 最大右边界
index 当前下标
array 数组和转换后的字符串一样长记录每个对应的位置的最大回文半径是多少
res 首先你要将整个字符串 QQ 转换成一个 #Q#Q# 类似的情况
也忒难了  我回头再看吧
"""


def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    pR = -1
    index = 0
    res = '#' + '#'.join(s) + '#'
    len_res = len(res)
    aArry = [0] * len_res
    len_r = 0
    max_r = ''
    for i in range(len_res):
        aArry[i] = min(pR - i, aArry[2 * index - i]) if pR > i else 1
        while i + aArry[i] < len_res and i - aArry[i] > -1:
            if res[i + aArry[i]] == res[i - aArry[i]]:
                aArry[i] += 1
            else:
                break
        if i + aArry[i] > pR:
            pR = i + aArry[i]
            index = i
        if len_r < aArry[i]:
            len_r = aArry[i]
            max_r = res[i - aArry[i] + 1: i + aArry[i]].replace('#', '')
    return max_r
