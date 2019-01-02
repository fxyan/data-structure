"""
归并排序
"""
def merge_sort(array):
    if len(array) < 2 or array is None:
        return array
    return sort_process(array, 0, len(array)-1)


def sort_process(array, l, r):
    if l < r:
        mid = int((r+l)/2)
        sort_process(array, l, mid)
        sort_process(array, mid+1, r)
        merge(array, l, mid, r)
    return array


def merge(array, l, mid, r):
    help = []
    left = l
    right = mid + 1
    while left <= mid and right <= r:
        if array[left] < array[right]:
            help.append(array[left])
            left += 1
        else:
            help.append(array[right])
            right += 1
    while left <= mid:
        help.append(array[left])
        left += 1
    while right <= r:
        help.append(array[right])
        right += 1
    for i in range(len(help)):
        array[l+i] = help[i]


def test_merge():
    array = [4, 2, 6, 1, 6, 5, 7]
    array1 = []
    array2 = [5]
    print(merge_sort(array))
    print(merge_sort(array1))
    print(merge_sort(array2))


"""
逆序对
"""
def reverse_order(array):
    if len(array) < 2 or array is None:
        return None
    return order(array, 0, len(array)-1)


def order(array, l, r):
    if l < r:
        mid = int((l+r)/2)
        return order(array, l, mid) + order(array, mid+1, r) + merge_order(array, l, mid, r)
    else:
        return []


def merge_order(array, l, mid, r):
    help = []
    order = []
    left = l
    right = mid + 1
    while left <= mid and right <= r:
        if array[left] <= array[right]:
            help.append(array[left])
            left += 1
        else:
            order.append([array[left], array[right]])
            help.append(array[right])
            right += 1
    while left <= mid:
        help.append(array[left])
        left += 1
    while right <= r:
        help.append(array[right])
        right += 1
    for i in range(len(help)):
        array[l+i] = help[i]
    return order


def test_revers():
    array = [4, 2, 6, 1]
    array1 = []
    array2 = [5]
    print(reverse_order(array))
    print(reverse_order(array1))
    print(reverse_order(array2))


if __name__ == '__main__':
    # test_merge()
    test_revers()