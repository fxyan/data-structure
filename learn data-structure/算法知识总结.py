"""
    一开始我没有具体的去系统的学习过算法对于基础的学习的都是直接看的代码实现，现在我在跟慕课，打算把上面的系统
知识保留到我的笔记上。在这里我只介绍算法思想，具体的实现在另外的文件进行

渐进分析:
    算法的时间复杂度就是这么算的，通过时间复杂度的公式去掉低阶项和前面的常数因子，得到我们需要的额时间复杂度
    简单的把公式这样进行拆分就能得到一般的时间复杂度      3N² + 2N + 9000 = N²
    在进行算法分析的时候要同时兼顾工程思维和数学思维，虽然从渐进分析来看高复杂度的算法确实优秀，但是在输入数据较少的时候
    才用高复杂度的一些算法却是最合适的。例如插入排序
    将一行语句在计算机中执行的时间称为 c

递归的时间复杂度分析:
    可以使用递归树，就像下面分析的那样
    可以使用主方法，不过有些限制
        a>1 子问题数量 b>1 要让子问题的输入减小 存在特定的n使f(n) > 0,于是在n足够大的时候是正数
        T(n) = aT(n/b) + f(n)
        计算 n log(b a) 的平方 和f(n)比较(假设f(n)为O(n的d次方))
        n log(b a) > d  O(n的log(b a)次方)
        n log(b a) = d  O(n的d次方乘log n)
        n log(b a) < d  O(n的d次方)
    可以使用递归树来确定主方法， 叶子结点的数量是a的h次方  h高为 log(b, n) 可以转化为 n 的次方 log(b a) 
"""
"""
分治模式一般分为三步
    先将大问题分解为比原问题规模要小的子问题
    计算子问题，如果子问题足够小直接计算，否则继续递归分解
    将子问题的解合并成原问题的解
归并排序标准的使用了这个思想
    先将原数组拆分成两个子数组
    将两个子数组按照递归的顺序进行排序
    将两个子数组合并排序成答案
        
归并排序可以使用递归树来进行具体的分析
                                        cn
                            cn/2                    cn/2                cn
                    cn/4            cn/4       cn/4         cn/4        cn
            .......................................................     叶子结点n
            高度因为是递归的所以是logn的
            总体就是 cnlogn + O(n) 使用渐进分析进行简化   nlogn 

还有简单的减而治之例如
a = [xx]
n = len(a)-1
x = 0
while n < 0:
    x += a[n]
    n -= 1
这问题能够被分成一个单独的子问题和剩余大块子问题，一直向下拆分直到剩余的大块子问题也变成单一的子问题，然后合并上面所有子问题
的和，这样也是一种递归思路 下面是递归例子
def sum1(xx):
    if len(xx) < 1:
        return 0
    else:
        c = xx.pop()
        return sum1(xx) + c
x = [1, 2, 3, 4, 5, 6, 7]
"""


"""
常见排序的稳定性
    稳定的 插入排序 
    非稳定 选择排序  快排 堆排序
    其中比较特殊的是归并和冒泡
            归并排序是可以做到稳定性的，你在merge的时候对于两个已经排序好的数组，你可以让子数组数据相等的时候选择左数组
        的数据加入到新数组，这样就实现了稳定。
            冒泡排序同样可以做到稳定性的，在两个值进行交换的时候可以进行优化，如果两个值的大小是相等的，那么就不进行交换
        这样实现了稳定
"""
# arrayA = [1, 3, 4, 12, 55, 56, 71, 81]
# arrayB = [2, 12, 13, 19, 32, 55, 57, 100]
# def merge(arrayA, arrayB):
#     a = len(arrayA)
#     b = len(arrayB)
#     A = 0
#     B = 0
#     help = []
#     while A < a and B < b:
#         if arrayA[A] < arrayB[B]:
#             help.append(arrayA[A])
#             A += 1
#         else:
#             help.append(arrayB[B])
#             B += 1
#     while A < a:
#         help.append(arrayA[A])
#         A += 1
#     while B < b:
#         help.append(arrayB[B])
#         B += 1
#     return help
# print(merge(arrayA, arrayB))