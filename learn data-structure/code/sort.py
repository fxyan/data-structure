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
    array2 = [5]
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
    array2 = [5]
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


if __name__ == '__main__':
    test_insert()
    test_bubble()
    test_select()
