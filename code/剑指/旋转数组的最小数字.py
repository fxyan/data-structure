"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

输入一个升序的数组的一个旋转，输出旋转数组的最小元素。

例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。

数组可能包含重复项。

注意：数组内所含元素非负，若数组大小为0，请返回-1。

样例
输入：nums=[2,2,2,0,1]

输出：0

这里注意可能数组没有被反转，还有可能第一个数值和最后一个数值相等，所以说要先过滤掉这种，然后二分    
"""

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        if len(nums) == 0:
            return -1
        while nums[l] == nums[r]:
            r -= 1
        if nums[l] < nums[r]:
            return nums[l]
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] < nums[0]:
                r = mid
            else:
                l = mid + 1
        return nums[l]

c = Solution()
c.findMin([2,2,2,0,1])