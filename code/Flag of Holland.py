"""
荷兰国旗问题主要就是基于快排的一个修改
"""


def flag(array, num):
    if len(array) < 2 or array is None:
        return array
    return sort(array, 0, len(array), num)


def sort(array, l, r, num):
    left = l - 1
    right = r
    while l < right:
        if array[l] < num:
            left += 1
            array[left], array[l] = array[l], array[left]
            l += 1
        elif array[l] > num:
            right -= 1
            array[right], array[l] = array[l], array[right]
        else:
            l += 1


def test():
    array = [3, 5, 1, 7, 4, 9, 6, 7, 10, 8, 96]
    flag(array, 7)
    print(array)


if __name__ == '__main__':
    test()
