"""
给定一个矩阵顺时针一圈一圈打印
"""

def order_print(array):
    tR = 0
    tC = 0
    dR = len(array) - 1
    dC = len(array[0]) - 1
    while tR <= dR and tC <= dC:
        print_edge(array, tR, tC, dR, dC)
        tR += 1
        tC += 1
        dR -= 1
        dC -= 1


def print_edge(array, tR, tC, dR, dC):
    if tR == dR:
        for i in range(tC, dC + 1):
            print(array[tR][i])
    elif tC == dC:
        for i in range(tR, dR + 1):
            print(array[i][tC])
    else:
        curR = tR
        curC = tC
        while curC != dC:
            print(array[curR][curC])
            curC += 1
        while curR != dR:
            print(array[curR][curC])
            curR += 1
        while curC != tC:
            print(array[curR][curC])
            curC -= 1
        while curR != tR:
            print(array[curR][curC])
            curR -= 1


"""
给定一个矩阵要求每个元素按照顺时针进行交换90度
 1, 2     交换后  3, 1
 3, 4             4, 2
"""


def rotate(array):
    tR = 0
    tC = 0
    dR = len(array) - 1
    dC = len(array[0]) - 1
    while tR <= dR and tC <= dC:
        rotate_edge(array, tR, tC, dR, dC)
        tC += 1
        tR += 1
        dC -= 1
        dR -= 1
    return array


def rotate_edge(array, tR, tC, dR, dC):
    size = dC - tC
    for i in range(size):
        time = array[tR][tC + i]
        array[tR][tC + i] = array[dR - i][tC]
        array[dR - i][tC] = array[dR][dC - i]
        array[dR][dC - i] = array[tR + i][dC]
        array[tR + i][dC] = time


"""
之字形打印
"""


def print_zhi(array):
    aR = 0
    aC = 0
    bR = 0
    bC = 0
    endR = len(array[0]) - 1
    endC = len(array) - 1
    bool_sign = True
    while aC <= endC:
        print_level(array, aR, aC, bR, bC, bool_sign)
        aC = aC if aR < endR else aC + 1
        aR = aR + 1 if aR < endR else aR
        bR = bR if bC < endC else bR + 1
        bC = bC + 1 if bC < endC else bC
        bool_sign = False if bool_sign else True
        # print('ar, ac', bR, bC)


def print_level(array, aR, aC, bR, bC, bool_sign):
    if bool_sign:
        print(array[bC][bR], end=' ')
        while aR != bR and aC != bC:
            bR += 1
            bC -= 1
            print(array[bC][bR], end=' ')
    else:
        print(array[aC][aR], end=' ')
        while aR != bR and aC != bC:
            aR -= 1
            aC += 1
            print(array[aC][aR], end=' ')


"""
判断链表是否是回文结构的不用辅助空间的算法
if head is None or head.next is None:
            return True
        n1 = head
        n2 = head
        while n2.next is not None and n2.next.next is not None:
            n1 = n1.next
            n2 = n2.next.next
        n2 = n1.next
        n3 = None
        n1.next = None
        while n2 is not None:
            n3 = n2.next
            n2.next = n1
            n1 = n2
            n2 = n3
        n3 = n1
        n2 = head
        res = True
        while n1 is not None and n2 is not None:
            if n1.val != n2.val:
                res = False
                break
            n1 = n1.next
            n2 = n2.next
        n1 = n3.next
        n3.next = None
        while n1 is not None:
            n2 = n1.next
            n1.next = n3
            n1 = n2
            n3 = n1
        return res 

"""
