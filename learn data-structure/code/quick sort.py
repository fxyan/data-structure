import random


def quick_sort(array):
    if len(array) < 2 or array is None:
        return array
    return quick(array, 0, len(array) - 1)


def quick(array, l, r):
    if l < r:
        rand = random.randint(l, r)
        array[r], array[rand] = array[rand], array[r]
        q = partition(array, l, r)
        quick(array, l, q - 1)
        quick(array, q + 1, r)


def partition(array, l, r):
    i = l - 1
    j = r
    while l < j:
        if array[l] < array[r]:
            i += 1
            array[i], array[l] = array[l], array[i]
            l += 1
        else:
            j -= 1
            array[j], array[l] = array[l], array[j]
    array[r], array[j] = array[j], array[r]
    return j


def test():
    array = [4, 2, 76, 1, 7, 2, 78]
    quick_sort(array)
    print(array)


def heapsort(array):
    if len(array) < 2 or array is None:
        return array
    build_max(array, len(array))
    for i in range(len(array)-1, -1, -1):
        print(array, i)
        array[0], array[i] = array[i], array[0]
        heap_insert(array, 0, i)


def build_max(array, r):
    for i in range((r-2)//2, -1, -1):
        heap_insert(array, i, r)


def heap_insert(array, root, r):
    left = root * 2 + 1
    while left < r:
        large = left if left+1 >= r or array[left] > array[left+1] else left + 1
        if array[large] > array[root]:
            array[large], array[root] = array[root], array[large]
            root = large
            left = root * 2 + 1
        else:
            break


def test_heap():
    array = [4, 2, 76, 1, 7, 2, 78]
    heapsort(array)
    print(array)


if __name__ == '__main__':
    test()
    test_heap()
