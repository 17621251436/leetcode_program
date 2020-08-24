##两数之和 lk 1
#给定一个整数数组 nums 和一个目标值 target，
# 请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp=[]
        if len(nums)==0:
            return []
        for i in  range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    tmp.append(i)
                    tmp.append(j)
                    break
        return tmp




##返回两个元素
        # nums.sort()
        # i=0
        # j=len(nums)-1
        # tmp=[]
        # while i<j:
        #     if nums[i]+nums[j]==target:
        #
        #         tmp.append(nums[i])
        #         tmp.append(nums[j])
        #         break
        #     elif  nums[i]+nums[j]>target:
        #
        #         j=j-1
        #
        #     else:
        #         i=i+1
        # return tmp