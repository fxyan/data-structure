"""
给定一个长度为 n 的整数数组 nums，数组中所有的数字都在 0∼n−1 的范围内。

数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。

请找出数组中任意一个重复的数字。

注意：如果某些数字不在 0∼n−1 的范围内，或数组中不包含重复数字，则返回 -1；

样例
给定 nums = [2, 3, 5, 4, 3, 2, 6, 7]。

返回 2 或 3。
"""


class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """
        # 哈希表法
        # if len(nums) is None:
        #     return -1
        # hash_n = {}
        # n = len(nums)
        # res = -1
        # for i in range(n):
        #     if nums[i] < 0:
        #         return -1
        #     if nums[i] not in hash_n:
        #         hash_n[nums[i]] = 1
        #     else:
        #         res = nums[i]
        # return res

        # 转换法
        n = len(nums)
        res = -1
        i = 0
        if n == 0:
            return res
        for i in range(n):
            if nums[i] < 0:
                return res
        while i < n:
            nums_i = nums[i]
            if nums[i] > n - 1 or nums[i] < 0:
                return -1
            if nums[i] == nums[nums_i] and i != nums_i:
                return nums[i]
            nums[i], nums[nums_i] = nums[nums_i], nums[i]
            if nums[i] == i:
                i += 1
        return res


c = Solution()

print(c.duplicateInArray([7, 6, 16, 8, 10, 3, 14, 1, 18, 4, 15, 9, 2, 0, 12, 5, 19, 13, 11, 17]))