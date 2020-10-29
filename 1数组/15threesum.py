#lk 15
#给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
# 使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left=0
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            left=i+1
            right=len(nums)-1
            if nums[i]+nums[left]+nums[left+1]>0:
                break
            if nums[i]+nums[right]+nums[right+1]<0:
                continue
            while left<right:
                a=[]



        # left=0
        # nums.sort()
        # for i in range(len(nums)-2):
        #     if i>0 and nums[i-1]==nums[i]:
        #         continue
        #     left=i+1
        #     right= len(nums)-1
        #     #剪枝
        #     if nums[i]+nums[left]+nums[left+1]>0:
        #         break
        #     if nums[i]+nums[right]+nums[right+1]<0:
        #         continue

        #     while left<right:
        #         a=[]
        #         if nums[i]+nums[left]+nums[right]==0:
        #             a.append(nums[i])
        #             a.append(nums[left])
        #             a.append(nums[right])
        #             left=left+1
        #             right=right-1
        #             tmp.append(a)
        #             while nums[left]==nums[left-1] and left<right:

        #                  left=left+1

        #             while nums[right] == nums[right + 1] and left<right:

        #                  right=right-1

        #         elif nums[i]+nums[left]+nums[right]>0:
        #             right=right-1
        #         else:
        #             left=left+1

        # return tmp