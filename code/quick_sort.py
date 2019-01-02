import random


# def quick_sort(array):
#     if len(array) < 2:
#         return array
#     else:
#         c = int(random.randint(0, len(array)-1))
#         array[0], array[c] = array[c], array[0]
#         cur = array[0]
#         left = [x for x in array[1:] if x < cur]
#         right = [x for x in array[1:] if x >= cur]
#         return quick_sort(left) + [cur] + quick_sort(right)

# def guoqi(x, 4):
#     quick_sort(x)

# def guoqi(array, x):
#     if len(array) < 2:
#         return array
#     else:
#         help = []
#         l = 0
#         r = len(array) - 1
#         for i in range(len(array)):
#             while l <= r:
#                 if array[l] < x:
#                     help.append()


def quick_interface(array):
    if len(array) < 2 and array is None:
        return array
    return quick_sort(array, 0, len(array)-1)


def quick_sort(array, l, r):
    if l < r:
        ran = random.randint(l, r)
        array[ran], array[r] = array[r], array[ran]
        p = partition(array, l, r)
        quick_sort(array, l, p[0]-1)
        quick_sort(array, p[1]+1, r)
    return array


def partition(array, l, r):
    less = l-1
    more = r
    while l < more:
        if array[l] < array[r]:
            less += 1
            array[l], array[less] = array[less], array[l]
            l += 1
        elif array[l] > array[r]:
            more -= 1
            array[l], array[more] = array[more], array[l]
        else:
            l += 1
    array[l], array[r] = array[r], array[l]
    p = [less + 1, more]
    return p


x = [3, 4, 1, 4, 76, 8, 1, 3, 3, 5, 7, 8, 3, 9, 0]
print(quick_interface(x))