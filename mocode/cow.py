    import sys
# c = [i for i in sys.stdin.readline().strip().split()]
ans = []
for i in range(2):
    # 读取每一行
    line = sys.stdin.readline().strip()
    print(line)
    print(line.split())
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))
    ans.append(values)
print(ans)

"""
list
min() max() sum() .index()

.remove(具体内容)  .pop(索引号)    del a[索引号]

.sort(key=lambda x: x[0])

.sort(key=lambda x:(-x[1],x[0],x[2]))#默认是升序，加个符号变降序，可做多级排序。

sorted()#不在本地做排序

元素 in list名称

变量
float('inf')无穷大 

字典
.keys()

.values()

.items()#返回的是元组

 

字符串
.strip() 去除首位空格

.strip().strip(‘-a’)去除首位空格和字符

S[:3]+S[5:] 拼接字符串，去除某个字符

.replace(‘a’,’b’) 替换字符

re.sub(‘a’,’b’,s) 替换字符

"""