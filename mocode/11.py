def iter_count(base_num, num, count):
    if base_num == num:
        return count
    if base_num * 2 > num:
        a = num - base_num - 1
        b = base_num * 2 - num
        return count + min(a, b)
    else:
        print(base_num, num, count)
        if num % 2 != 0:
            count += 1
        return iter_count(base_num, num // 2, count + 1)


def count_num(l_num):
    count = 0
    l_num.sort()
    if l_num[1] <= 0:
        return l_num[1] - l_num[0]
    if l_num[0] < 0:
        count += 1 - l_num[0]
    return iter_count(l_num[0], l_num[1], count)

# print(count_num([2, 6]))
c = '3-'
if '-' in c:
    print(1)