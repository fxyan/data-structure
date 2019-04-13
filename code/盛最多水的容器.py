"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

使用双指针的方法解决它 左右端点各为指针 maxarea设定为最大容积初始为0
每次循环计算两个端点中较短的哪一个到另一端点的蓄水量 然后对比maxarea进行更新
然后将较小的端点移动
"""


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxarea = 0
    l = 0
    r = len(height)-1
    while l < r:
        maxarea = max(maxarea, min(height[l], height[r])*(r-l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maxarea