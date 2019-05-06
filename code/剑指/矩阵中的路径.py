"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。

路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。

如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。

注意：

输入的路径不为空；
所有出现的字符均为大写英文字母；
样例
matrix=
[
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]

str="BCCE" , return "true"

str="ASAE" , return "false"

解法，暴搜，从每一个位置开始深搜
"""


class Solution(object):
    def hasPath(self, matrix, string):
        """
        :type matrix: List[List[str]]
        :type string: str
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        self.col = len(matrix)
        self.raw = len(matrix[0])
        for i in range(self.col):
            for j in range(self.raw):
                if matrix[i][j] == string[0]:
                    self.b = False
                    dict = []
                    dict += [[i, j]]
                    self.dfs(matrix, i, j, dict, string[1:])
                    if self.b:
                        return True
        return False

    def dfs(self, matrix, c, r, dict, string):
        if string == '':
            self.b = True
            return
        if c != 0 and [c-1, r] not in dict and matrix[c-1][r] == string[0]:
            dict += [[c-1, r]]
            self.dfs(matrix, c-1, r, dict, string[1:])
        if r != 0 and [c, r-1] not in dict and matrix[c][r-1] == string[0]:
            dict += [[c, r-1]]
            self.dfs(matrix, c, r-1, dict, string[1:])
        if c != self.col-1 and [c+1, r] not in dict and matrix[c+1][r] == string[0]:
            dict += [[c+1, r]]
            self.dfs(matrix, c+1, r, dict, string[1:])
        if r != self.raw-1 and [c, r+1] not in dict and matrix[c][r+1] == string[0]:
            dict += [[c, r+1]]
            self.dfs(matrix, c, r+1, dict, string[1:])