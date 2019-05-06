# 并查集
"""
首先用两个哈希表来确定
一个哈希表来记录父节点
data 表示节点
hash_father = {data: data}
一个哈希表来记录整个并查集的大小
hash_size = {data: size}
如果查询加合并的次数超过n次那么并查集的平均复杂度是O(1)的
"""


class UnionFindSet():
    def __init__(self, node):
        self.hash_father = {}
        self.hash_size = {}
        self.make_set(node)

    def make_set(self, node):
        self.hash_father.clear()
        self.hash_size.clear()
        for i in node:
            self.hash_father[i] = i
            self.hash_size[i] = 1

    def data_find_head(self, node):
        father = self.hash_father.get(node)
        if father != node:
            father = self.data_find_head(father)
        self.hash_father[node] = father
        return father

    def is_same_set(self, node1, node2):
        return self.data_find_head(node1) == self.data_find_head(node2)

    def union(self, a, b):
        if a is None or b is None:
            return
        head_a = self.data_find_head(a)
        head_b = self.data_find_head(b)
        if head_b != head_a:
            size_a = self.hash_size[head_a]
            size_b = self.hash_size[head_b]
            if size_a >= size_b:
                self.hash_father[head_b] = head_a
                self.hash_size[head_a] = size_b + size_a
            else:
                self.hash_father[head_a] = head_b
                self.hash_size[head_b] = size_b + size_a


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    union_find_set = UnionFindSet(a)
    union_find_set.union(1, 2)
    print(union_find_set.is_same_set(2, 1))
    union_find_set.union(3, 5)
    union_find_set.union(3, 1)
    print(union_find_set.is_same_set(2, 5))  # True