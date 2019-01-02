"""
堆排序的边界很恶心，因为数组下标从0开始的，
left = root * 2 + 1
right = left + 1

parent = left / 2
parent = right / 2 -1

从 len(array) - 2 // 2 才是非叶子节点的最后一个

"""


def heap_sort(array):
    len_array = len(array)
    build_max_heap(array, len_array)
    for i in range(len_array - 1, -1, -1):
        array[0], array[i] = array[i], array[0]
        max_heap(array, i, 0)


def build_max_heap(array, len_array):
    for i in range((len_array-2)//2, -1, -1):
        max_heap(array, len_array, i)
    return array


def max_heap(array, i, root):
    large = root
    left = 2 * root + 1
    right = left + 1
    len_array = i - 1
    if left <= len_array and array[left] > array[large]:
        large = left
    if right <= len_array and array[right] > array[large]:
        large = right
    if large != root:
        array[large], array[root] = array[root], array[large]
        return max_heap(array, len_array, large)

"""
循环的堆排序感觉会好一点
def heap_sort(array):
    if len(array) < 2 or array is None:
        return array
    size = len(array)
    build_max(array, size)
    for i in range(size-1, -1, -1):
        array[i], array[0] = array[0], array[i]
        heap_insert(array, 0, i)


def build_max(array, size):
    for i in range((size-2)//2, -1, -1):
        heap_insert(array, i, size)


def heap_insert(array, root, size):
    left = root * 2 + 1
    while left < size:
        largest = left+1 if left+1 < size and array[left+1] > array[left] else left
        if array[root] < array[largest]:
            array[root], array[largest] = array[largest], array[root]
            root = largest
            left = root * 2 + 1
        else:
            return


def test_heap():
    array = [4, 2, 1, 7, 5, 3, 2, 4]
    array2 = [4, 4, 1]
    heap_sort(array)
    heap_sort(array2)
    print(array)
    print(array2)
"""


def test():
    array = [2, 12, 42, 43, 23, 1, 0]
    heap_sort(array)
    print(array)


if __name__ == '__main__':
    test()