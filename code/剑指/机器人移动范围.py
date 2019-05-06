"""
地上有一个 m 行和 n 列的方格，横纵坐标范围分别是 0∼m−1 和 0∼n−1。
一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格。
但是不能进入行坐标和列坐标的数位之和大于 k 的格子。
请问该机器人能够达到多少个格子？

样例1
输入：k=7, m=4, n=5

输出：20
样例2
输入：k=18, m=40, n=40

输出：1484

解释：当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
      但是，它不能进入方格（35,38），因为3+5+3+8 = 19。

这里还是用了深搜
"""


class Solution(object):
    def movingCount(self, threshold, rows, cols):
        """
        :type threshold: int
        :type rows: int
        :type cols: int
        :rtype: int
        """
        self.rows = rows
        self.cols = cols
        self.dict = set()
        self.search(threshold, 0, 0)
        return len(self.dict)

    def judge(self, threshold, c, r):
        return sum(map(int, list(str(c)))) + sum(map(int, list(str(r)))) <= threshold

    def search(self, threshold, c, r):
        if not self.judge(threshold, c, r) or (c, r) in self.dict:
            return
        self.dict.add((c, r))
        if c < self.cols - 1:
            self.search(threshold, c+1, r)
        if r < self.rows - 1:
            self.search(threshold, c, r+1)