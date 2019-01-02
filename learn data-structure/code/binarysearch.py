def binary_search(array, intage):
    if len(array) is None:
        return None
    lo = 0
    r = len(array) - 1
    while lo <= r:
        mid = (lo+r) // 2
        if intage < array[mid]:
            r = mid - 1
        elif intage > array[mid]:
            lo = mid + 1
        else:
            return array[mid]
    return -1


def test():
    array = [1, 2, 54, 66, 5943, 3845739]
    print(binary_search(array, 1))


if __name__ == '__main__':
    # test()
    pass