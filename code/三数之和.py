"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组

一开始和三数之和是一样的
不过要注意i j k三个值变换之后会不会和没变换时相同
"""


def threeSum(nums):
    nums.sort()
    res = []
    len_nums = len(nums)
    for i in range(len_nums - 2):
        k = len(nums) - 1
        j = i + 1
        if i > 0 and nums[i] == nums[i-1]:
            continue
        while j < k:
            if nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while nums[j] == nums[j-1] and j < k:
                    j += 1
                while nums[k] == nums[k+1] and k > j:
                    k -= 1
    return res


print(threeSum([-1,0,1,2,-1,-4]))