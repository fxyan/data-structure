def rank(key):
    c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    l = 0
    r = len(c) - 1
    while l <= r:
        mid = int(l + (r - l) / 2)
        if key < c[mid]:
            r = mid - 1
        elif key > c[mid]:
            l = mid + 1
        else:
            return 1
    return -1


def main():
    key = input('请输入要查询的key：')
    if rank(int(key)) < 0:
        return key
    return '存在'


if __name__ == '__main__':
    print(main())
