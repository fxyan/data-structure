# 定长的列表
class Array(object):
    def __init__(self, size=8):
        self._size = size
        self._item = [None] * size

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        return self._item[index]

    def __setitem__(self, key, value):
        self._item[key] = value

    def clear(self, value=None):
        for i in range(len(self._item)):
            self._item[i] = value

    def __iter__(self):
        for item in self._item:
            yield item

    def __repr__(self):
        return '列表值: {}'.format(self._item)

print(Array())
