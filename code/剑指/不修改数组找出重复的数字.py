"""
给定一个长度为 n+1 的数组nums，数组中所有的数均在 1∼n 的范围内，其中 n≥1。

请找出数组中任意一个重复的数，但不能修改输入的数组。

样例
给定 nums = [2, 3, 5, 4, 3, 2, 6, 7]。

返回 2 或 3。
思考题：如果只能使用 O(1) 的额外空间，该怎么做呢？
如果额外空间是O(1)那么可以使用抽屉原则
"""

class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """
        size = len(nums)
        if size == 0:
            return None
        l = 1
        r = size - 1
        while l < r:
            mid = l + (r-l)//2
            s = 0
            for i in range(size):
                if nums[i] >= l and nums[i] <= mid:
                    s += 1
                if s >= mid - l + 1:
                    r = mid
                else:
                    l = mid + 1
        return r
s = [1,2,3,4]
print(s[0:])