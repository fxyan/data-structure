"""
插入排序
    一般假设第一个数是一个序列，从第二个数开始进行排序，将第二个数开始插入到队列中去，先看插入的数据是否比队列结尾的数
    要大如果大的话就不动将数据插到序列结尾，如果小的话就将序列末尾的数据后移一位，然后继续比较直到插入的数据已经到了
    序列对应的位置或者已经到头了。
    插入排序如果遇到了正好的反向序列是十分慢的，但是如果遇到的部分有序的队列速度就十分快，可以利用插入排序的性质来进行
    选择使用
    写代码的时候注意要有一个中间变量index来记录当前交换的下标
"""


def insert_sort(array):
    size = len(array)
    if size == 1 or array is None:
        return array
    return sort(array, size)


def sort(array, size):
    for i in range(1, size):
        index = i
        j = i
        while j > 0 and array[j] < array[j-1]:
            j -= 1
            array[index], array[j] = array[j], array[index]
            index -= 1
    return array


if __name__ == '__main__':
    array = [3, 4, 5, 1, 7, 984, 34, 11]
    array1 = []
    array2 = [1]
    print(insert_sort(array))
    print(insert_sort(array1))
    print(insert_sort(array2))