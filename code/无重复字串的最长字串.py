"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
思路是这样的 
last = -1
先用哈希表接住所有的字母，然后判断是不是重复的如果是更新last不是的话
记录maxlen
更新哈希表
"""


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    hash = {}
    maxlen = 0
    last = -1
    for i, x in enumerate(s):
        if x in hash and hash[x] > last:
            last = hash[x]
        maxlen = max(maxlen, i - last)
        hash[x] = i
    return maxlen

