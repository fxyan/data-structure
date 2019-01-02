"""
# 小和问题
def merge_sort(array):
    if array is None or len(array) < 2:
        return array
    return sort_process(array, 0, len(array)-1)


def sort_process(array, l, r):
    if l == r:
        return 0
    else:
        mid = int((l + r) / 2)
        # sort_process(array, l, mid)
        # sort_process(array, mid+1, r)
        # merge(array, l, mid, r)
    # return array
    return sort_process(array, l, mid) + sort_process(array, mid+1, r) + merge(array, l, mid, r)


def merge(array, l, mid, r):
    help = []
    a = l
    b = mid + 1
    c = 0
    while a <= mid and b <= r:
        if array[a] < array[b]:
            c += array[a] * (r - b + 1)
            help.append(array[a])
            a += 1
        else:
            if array[a] != array[b]:
                print(array[a], array[b])
            help.append(array[b])
            b += 1
    while a <= mid:
        help.append(array[a])
        a += 1
    while b <= r:
        help.append(array[b])
        b += 1
    for i in range(len(help)):
        array[l+i] = help[i]
    return c


x = [4, 2, 9, 3, 5, 2, 6, 3]
print(merge_sort(x))
"""

"""
def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


def select_sort(array):
    for i in range(len(array)-1):
        index = i
        for j in range(i+1, len(array)):
            if array[index] > array[j]:
                index = j
        if index != i:
            array[index], array[i] = array[i], array[index]
    return array


def inser_sort(array):
    for i in range(1, len(array)):
        index = i
        value = array[i]
        while index > 0 and value < array[index-1]:
            array[index] = array[index-1]
            index -= 1
        if index != i:
            array[index] = value
    return array
"""


"""
def merge_sort(array):
    if len(array) < 2 and array is None:
        return array
    return sore_process(array, 0, len(array)-1)


def sore_process(array, l, r):
    if l == r:
        return None
    else:
        mid = int((l + r) / 2)
        sore_process(array, l, mid)
        sore_process(array, mid+1, r)
        merge(array, l, mid, r)
    return array


def merge(array, l, mid, r):
    help = []
    a = l
    b = mid + 1
    while a <= mid and b <= r:
        if array[a] < array[b]:
            help.append(array[a])
            a += 1
        else:
            help.append(array[b])
            b += 1
    while a <= mid:
        help.append(array[a])
        a += 1
    while b <= r:
        help.append(array[b])
        b += 1
    for i in range(len(help)):
        array[l+i] = help[i]


x = [4, 2, 9, 3, 5, 2, 6, 3]
print(merge_sort(x))
"""

def heap_sort(array):
    if len(array) < 2 and array is None:
        return array
    else:
        return heap_process(array)


def heap_process(array):
    for i in range(len(array)):
        heap_insert(array, i)
    for i in range(len(array)-1, -1, -1):
        array[i], array[0] = array[0], array[i]
        heapfiy(array, i, 0)
    return array


def heap_insert(array, index):
    while array[index] > array[int((index-1) / 2)]:
        array[index], array[int((index-1) / 2)] = array[int((index-1) / 2)], array[index]
        index = int((index - 1) / 2)


def heapfiy(array, l, root):
    left = 2 * root + 1
    right = left + 1
    large = root
    if left < l and array[large] < array[left]:
        large = left
    if right < l and array[large] < array[right]:
        large = right
    if large != root:
        array[large], array[root] = array[root], array[large]
        heapfiy(array, l, large)


x = [4, 2, 9, 3, 5, 2, 6, 3]
print(heap_sort(x))