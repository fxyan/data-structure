def insert_sort(array):
    len_array = len(array)
    if len_array < 2 and array is None:
        return array
    for i in range(1, len_array):
        index = i
        value = array[i]
        while index > 0 and value < array[index - 1]:
            array[index] = array[index - 1]
            index -= 1
        array[index] = value
    return array


def test_insert():
    array = [4, 2, 6, 1, 6, 5, 7]
    array1 = []
    array2 = [7, 5]
    print(insert_sort(array))
    print(insert_sort(array1))
    print(insert_sort(array2))


def bubble_sort(array):
    len_array = len(array)
    if len_array < 2 or array is None:
        return array
    for i in range(len_array - 1):
        for j in range(len_array - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def test_bubble():
    array = [4, 2, 6, 1, 6, 5, 7]
    array1 = []
    array2 = [8, 5]
    print(bubble_sort(array))
    print(bubble_sort(array1))
    print(bubble_sort(array2))


def select_sort(array):
    if array is None or len(array) < 2:
        return array
    for i in range(len(array)-1):
        minindex = i
        for j in range(i+1, len(array)):
            if array[j] < array[minindex]:
                minindex = j
        if minindex != i:
            array[i], array[minindex] = array[minindex], array[i]
    return array


def test_select():
    array = [4, 2, 6, 1, 6, 5, 7]
    array1 = []
    array2 = [5]
    select_sort(array)
    select_sort(array1)
    select_sort(array2)
    print(array)
    print(array1)
    print(array2)


def merge_sort(array):
    if len(array) < 1 or array is None:
        return array
    return merge_part(array, 0, len(array)-1)


def merge_part(array, l, r):
    if l == r:
        return None
    mid = (l + r)//2
    merge_part(array, l, mid)
    merge_part(array, mid+1, r)
    merge(array, l, mid, r)
    return array


def merge(array, l, mid, r):
    help = []
    left = l
    right = mid+1
    while left <= mid and right <= r:
        if array[left] <= array[right]:
            help.append(array[left])
            left += 1
        else:
            help.append(array[right])
            right += 1
    while left <= mid:
        help.append(array[left])
        left += 1
    while right <= mid:
        help.append(array[right])
        right += 1
    for i in range(len(help)):
        array[l+i] = help[i]


def test_merge():
    array = [4, 2, 6, 1, 6, 5, 7]
    array1 = []
    array2 = [8, 5]
    print(merge_sort(array))
    print(merge_sort(array1))
    print(merge_sort(array2))


import random
def quick_sort(array):
    if len(array) < 1 or array is None:
        return array
    return quick_deal_with(array, 0, len(array)-1)


def quick_deal_with(array, l, r):
    if l < r:
        rand = random.randint(1, r)
        array[rand], array[r] = array[r], array[rand]
        mid = partition(array, l, r)
        quick_deal_with(array, l, mid[0]-1)
        quick_deal_with(array, mid[1]+1, r)
    return array


def partition(array, l, r):
    left = l - 1
    right = r
    size = l
    while size < right:
        if array[size] < array[r]:
            left += 1
            array[size], array[left] = array[left], array[size]
            size += 1
        elif array[size] > array[r]:
            right -= 1
            array[size], array[right] = array[right], array[size]
        else:
            size += 1
    array[r], array[right] = array[right], array[r]
    p = [left+1, right]
    return p


def test_quick_sort():
    array = [4, 2, 6, 1, 6, 5, 7]
    array1 = []
    array2 = [8, 5]
    print(quick_sort(array))
    print(quick_sort(array1))
    print(quick_sort(array2))


def heap_sort(array):
    if len(array) < 1 or array is None:
        return array
    return heap_process(array)

def heap_process(array):
    length = len(array)
    for i in range(length):
        heap_insert(array, i)
    heapsize = len(array) - 1
    while heapsize > 0:
        array[0], array[heapsize] = array[heapsize], array[0]
        heapsize -= 1
        # print('1', heapsize)
        heapfiy(array, 0, heapsize)
        # print('2', array)
    return array


def heap_insert(array, index):
    while array[index] > array[int((index-1)/2)]:
        array[index], array[(index-1)//2] = array[(index-1)//2], array[index]
        index = int((index-1)/2)


def heapfiy(array, l, r):
    left = 2 * l + 1
    while left <= r:
        right = left + 1
        largest = right if right <= r and array[left] < array[right] else left
        if largest == l:
            break
        array[largest], array[l] = array[l], array[largest]
        l = largest
        left = 2 * largest + 1


def test_heap():
    array = [4, 2, 6, 1, 6, 5, 7]
    array1 = []
    array2 = [8, 5]
    print(heap_sort(array))
    print(heap_sort(array1))
    print(heap_sort(array2))

if __name__ == '__main__':
    # test_insert()
    # test_bubble()
    # test_select()
    # test_merge()
    # test_quick_sort()
    test_heap()