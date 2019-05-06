def change_array(array_len):
    for i in range(len(array_len)):
        array = array_len[1]
        if len(array) == 0 or len(array) == 1:
            print('Yes')
        i = 0
        c = 1
        while i+1 < len(array) - 1:
            if array[i] == array[i + 1] == array[i + 2]:
                print('No')
            if array[i] > array[i+1] and array[i] > array[i+2] :
                if array[i+1] > array[i+2]:
                    c -= 1
                    if c < 0:
                        print('No')
                if array[i+1] < array[i+2]:
                    print('No')
            elif array[i] > array[i+1]:
                c -= 1
                if c < 0:
                    print('No')
            i += 1
        print('Yes')



class HashTable(object):
    def __init__(self, size):
        self.table_size = size
        self.table = [0] * self.table_size

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
                n += ord(i) * f
                f *= 10
            return n






if __name__ == '__main__':
    ans = []
    for i in range(1):
        c = input()
        c = c.split('/')
        j, k = int(c[0]), c[1]
        ans.append(j)
        if '-' in k:
            z = k.split('-')
            h, l = z[0], z[1]
            ans.append(h)
            if ',' in l:
                w = l.split(',')
                r, t = w[0], w[1]
                ans.append(r)
                ans.append(t)
    ans = [int(i) for i in ans]
    print(ans)
    # change_array(ans)
