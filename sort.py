# 冒泡排序
def bubble_sort(seq):
    n = len(seq)
    for i in range(n - 1):  # 不需要遍历到最后一位因为要和j+1进行比较
        for j in range(n - i - 1):  # 后面的i已经被排序完成了所以我们就不需要进行比较了
            if seq[j] > seq[j + 1]:  # 判断大小
                seq[j], seq[j + 1] = seq[j + 1], seq[j]  # 交换位置
    print(seq)


# 选择排序
def select_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        min_idx = i  # 确定最小值的index
        for j in range(i + 1, n):  # 遍历除了最小值以外的值
            if seq[j] < seq[min_idx]:
                min_idx = j  # 修改最小值index
        if min_idx != i:
            seq[i], seq[min_idx] = seq[min_idx], seq[i]
    print(seq)


# 插入排序
# 在排序好的序列中从后面插入一个数字如果它比前面的小就一直前移到合适位置
def insert_sort(seq):
    n = len(seq)
    for i in range(1, n):  # 我们从第二个数开始'插入'
        value = seq[i]  # 保存一下值
        pos = i  # 保存一下下标
        while pos > 0 and value < seq[pos - 1]:  # 如果插入的数字比前面的数字小就一直前移
            seq[pos] = seq[pos - 1]
            pos -= 1
        seq[pos] = value  # 在合适的位置给赋值
    print(seq)


# 归并排序
def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        mid = int(len(seq) / 2)
        left_half = merge_sort(seq[:mid])
        right_half = merge_sort(seq[mid:])
        # 合并数组
        new_seq = merge_sort_list(left_half, right_half)
        return new_seq


def merge_sort_list(sorted_a, sorted_b):
    length_a, length_b = len(sorted_a), len(sorted_b)
    a = b = 0
    new_sorted_seq = list()
    while a < length_a and b < length_b:
        if sorted_a[a] < sorted_b[b]:
            new_sorted_seq.append(sorted_a[a])
            a += 1
        else:
            new_sorted_seq.append(sorted_b[b])
            b += 1

    while a < length_a:
        new_sorted_seq.append(sorted_a[a])
        a += 1

    while b < length_b:
        new_sorted_seq.append(sorted_b[b])
        b += 1
    return new_sorted_seq


# 简陋版快速排序有两个缺点
def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot_index = 0
        pivot = array[pivot_index]
        less_part = [i for i in array[pivot_index+1:] if i <= pivot]
        great_part = [i for i in array[pivot_index+1:] if i > pivot]
        return quick_sort(less_part) + [pivot] + quick_sort(great_part)


def partition(array, beg, end):
    pivot_index = beg
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end - 1

    while True:
        while left <= right and array[left] < pivot:
            left += 1
        while right >= left and array[right] > pivot:
            right -= 1
        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]
    array[pivot_index], array[right] = array[right], array[pivot_index]
    return right


def quicksort_inplace(array, beg, end):
    if beg < end:
        pivot = partition(array, beg, end)
        quicksort_inplace(array, beg, pivot)
        quicksort_inplace(array, pivot+1, end)


def test_bubble_sort():
    seq = [1, 3, 2, 6, 0, 6, 3, 7, 9, 4]
    bubble_sort(seq)


def test_select_sort():
    seq = [1, 3, 2, 6, 0, 6, 3, 7, 9, 4]
    select_sort(seq)


def test_insert_sort():
    seq = [1, 3, 2, 6, 0, 6, 3, 7, 9, 4]
    insert_sort(seq)


if __name__ == '__main__':
    test_bubble_sort()
    test_select_sort()
    test_insert_sort()
    print(merge_sort([1, 3, 2, 6, 0, 6, 3, 7, 9, 4]))
    print(quick_sort([1, 3, 2, 6, 0, 6, 3, 7, 9, 4]))
