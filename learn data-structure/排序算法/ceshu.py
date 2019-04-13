import random


def quick_sort(array):
    if array is None or len(array) < 0:
        return array
    return quick(array, 0, len(array)-1)


def quick(array, l, r):
    if l < r:
        num = random.randint(l, r)
        array[num], array[r] = array[r], array[num]
        q = partition(array, l, r)
        quick(array, l, q-1)
        quick(array, q+1, r)


def partition(array, l, r):
    i = l-1
    j = r
    while l < j:
        if array[l] > array[r]:
            i += 1
            array[l], array[i] = array[i], array[l]
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


if __name__ == '__main__':
    test()