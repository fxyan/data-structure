"""
首先在一个列表中找到最小的元素，然后将它和列表中第一个元素交换，然后从剩余的列表中找到最小的元素，
然后和列表中的第二个元素进行交换。。。。。以此类推最后得到一个已经排序完成的列表

在进行编程的时候要注意 第一个for循环的时候保留min值 然后外层循环不需要循环到最后一个循环到倒是第二个就行
"""


def select_sort(array):
    size = len(array)
    if size == 1 or array is None:
        return array
    return sort(array, size)


def sort(array, size):
    for i in range(size-1):
        min = i
        for j in range(i+1, size):
            if array[j] < array[min]:
                min = j
        if min != i:
            array[i], array[min] = array[min], array[i]
    return array


if __name__ == '__main__':
    array = [3, 4, 5, 1, 7, 984, 34, 11]
    array1 = []
    array2 = [1]
    print(select_sort(array))
    print(select_sort(array1))
    print(select_sort(array2))
