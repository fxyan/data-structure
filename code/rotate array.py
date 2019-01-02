# 二分查找的思路 将整个旋转的数组看成是两个数组
# 找中点，如果中点比数组第一个大那么还在第一个数组中left=mid+1
# 这样循环left最终会变成第二个数组的第一个值也就是答案
# 如果中点比right小就把right=mid
# 跳出条件就是left >= right
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        elif len(rotateArray) == 1:
            return rotateArray[0]
        else:
            left = 0
            right = len(rotateArray)-1
            while left < right:
                mid = int((left + right)/2)
                print(mid)
                if rotateArray[mid] < rotateArray[right]:
                    right = mid
                else:
                    left = mid + 1
                    print('right', right)
            return rotateArray[right]

p = Solution()
print(p.minNumberInRotateArray([4, 5, 6, 7, 8, 9, 1, 2, 3]))