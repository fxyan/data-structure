"""
用中间数组来记录每个值的数量，然后通过累加来计算在新数组的下标
计数排序还是要注意边界,假设你数组的一共元素是7个但是数组下标 是从0开始的所以最后要-1
A为原数组
B排序结束后的数组
c为中间数组

k是原数组的最大值+1因为要包括0

"""


def counting_sort(A, B, k):
    c = []
    for i in range(k):
        c.append(0)
    for i in range(len(A)):
        c[A[i]] = c[A[i]] + 1
    for i in range(k):
        if i != 0:
            c[i] = c[i] + c[i-1]
    for i in range(len(A)):
        B[c[A[i]] - 1] = A[i]  # 特别注意这里的边界条件因为总的元素个数是要比数组下标多一的，
    # 因为数组下标是从0开始的
        c[A[i]] = c[A[i]] - 1


def test():
    array = [0, 2, 5, 2, 3, 1, 16, 42]
    array2 = [None, None, None, None, None, None, None, None]
    counting_sort(array, array2, max(array)+1)
    print(array2)


if __name__ == '__main__':
    test()
