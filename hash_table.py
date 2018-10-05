class HashTable(object):
    def __init__(self):
        # 哈希表首先让他有20007个格子
        # 让这个格子保持为素数能够获得更好的分布
        self.table_size = 20007
        self.table = [0] * self.table_size

    def __contains__(self, item):
        return self.has_key(item)

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, item):
        if item not in self:
            raise KeyError()
        else:
            return self.get(item)

    # 判断是不是有key
    def has_key(self, key):
        index = self._index(key)
        v = self.table[index]
        if isinstance(v, list):
            for kv in v:
                if kv[0] == key:
                    return True
        return False

    # 添加元素的具体操作
    def _insert_at_index(self, index, key, value):
        data = [key, value]
        # 找出下标的值
        v = self.table[index]
        # 这里判断如果值是int的话就是没有储存值的
        if isinstance(v, int):
            self.table[index] = [data]
        # 否则的话就是已经储存了我们使用链表法进行增加
        else:
            self.table[index].append(data)

    # 增加一个元素
    def add(self, key, value):
        # 先算出下标
        index = self._index(key)
        # 添加元素
        self._insert_at_index(index, key, value)

    # 得到key的值
    def get(self, key, default_value=None):
        index = self._index(key)
        v = self.table[index]
        if isinstance(v, list):
            for kv in v:
                if kv[0] == key:
                    return kv[1]
        return default_value

    # 来判断下标
    def _index(self, key):
        return self._hash(key) % self.table_size

    # 哈希函数来将key的值转化成一串数字
    def _hash(self, key):
        n = 0
        f = 1
        for i in key:
            n = ord(i) * f
            f *= 10
        return n

    # 遍历一下哈希表返回不为空的数
    def _iter_slot(self):
        for slot in self.table:
            if isinstance(slot, list):
                yield slot

    def items(self):
        for slot in self._iter_slot():
            for item in slot:
                yield (item[0], item[1])

    def keys(self):
        for slot in self._iter_slot():
            for item in slot:
                yield (item[0])

    def values(self):
        for slot in self._iter_slot():
            for item in slot:
                yield (item[1])



def test():
    import uuid
    names = [
        'gua',
        'xiao',
        'name',
        'web',
        'python',
    ]
    ht = HashTable()
    for key in names:
        value = uuid.uuid4()
        ht.add(key, value)
        print('add 元素', key, value)
    for key in names:
        v = ht.get(key)
        print('get 元素', key, v)
    ht.items()
    for i in ht.values():
        print(i)
    ht['wang'] = 23333
    print(ht['wang'])


if __name__ == '__main__':
    test()

