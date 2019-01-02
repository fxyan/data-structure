"""
一个无序数组，求排序之后相邻之间的值之间的最大差值，要求时间复杂读为O(N)
思路，使用桶排序，建立三个数组长度为array+1的数组分别是布尔 最大 最小
将每个数分别加入这三个数组中如果 这个值有数那么布尔为1， 最后取两个桶相邻之间的的最大值最小值的差值
"""


def maxgap(array):
    if len(array) < 2 and array is None:
        return array
    max_array = max(array)
    min_array = min(array)
    if max_array == min_array:
        return 0
    bool_list = [0] * (len(array) + 1)
    max_list = [None] * (len(array) + 1)
    min_list = [None] * (len(array) + 1)
    for i in range(len(array)):
        bid = bucket(array[i], len(array), max_array, min_array)
        max_list[bid] = max(max_list[bid], array[i]) if max_list[bid] is not None else array[i]
        min_list[bid] = min(min_list[bid], array[i]) if min_list[bid] is not None else array[i]
        bool_list[bid] = 1
    res = 0
    lastmax = max_list[0]
    for i in range(1, len(array)+1):
        if bool_list[i]:
            res = max(res, min_list[i] - lastmax)
            lastmax = max_list[i]
    return res


"""
首先(max - min) // len的值是每个桶的容量
(num - min) // 每个桶的容量就是桶号
"""
def bucket(num, len, max, min):
    return int((num - min) * len / (max - min))


print(maxgap([1, 4, 5, 0, 45, 20]))
