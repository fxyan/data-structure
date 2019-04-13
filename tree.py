"""
满二叉树 就是所有节点就要满的，不能有空缺节点
完全二叉树 除了最后一层叶子结点要求不同其余和满二叉树一样， 叶子结点都是从左到右的中间不能有空缺
二叉搜索树 左子树都比他小 右子树都比他大  插入数据就是比较大小找到不能再找的位置然后然后插入
"""
def threesum(array, length, res):
    val = 1
    for i in range(length-2):
        if i == 0 or array[i] > array[i-1]:
            k = length - 1
            j = i + 1
            while j < k:
                if array[i] + array[j] + array[k] == res:
                    print(array[i], array[j], array[k])
                    j += 1
                    k -= 1
                    while j < k and array[j] == array[j-1]:
                        j += 1
                    while k > j and array[k] == array[k+1]:
                        k -= 1
                    val = 0
                elif array[i] + array[j] + array[k] < res:
                    j += 1
                elif array[i] + array[j] + array[k] > res:
                    k -= 1
    if val == 1:
        print(-1, -1, -1)

if __name__ == "__main__":
    ans = []
    for i in range(2):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        ans.append(values)
    threesum(ans[1], ans[0][0], ans[0][1])



