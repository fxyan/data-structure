"""
class Array(object):
    def __init__(self, size=40):
        self.size = size
        self._item = [None] * size

    def __len__(self):
        return self.size

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
        return '{}'.format(self._item)


xx = Array(size=8)
xx[0] = 9
xx[1] = 3
for i in xx:
    print(i)

"""

#encoding:UTF-8
def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=",i)
    #做一些其它的事情
    print("do something.")
    print("end.")

def call(i):
    return i*2

#使用for循环
for i in yield_test(5):
    print(i,",")
