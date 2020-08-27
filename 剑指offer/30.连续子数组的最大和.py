class Solution(object):
    def maxSubArray(self, nums):
        maxNum=0
        sumNum=0
        if max(nums)<0:
            return max(nums)
        for num in nums:
            sumNum+=num
            maxNum=max(maxNum,sumNum)
            if sumNum<0:
                sumNum=0
        return maxNum