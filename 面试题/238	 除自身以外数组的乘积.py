class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        b = [1] * len(nums)
        tmp = 1
        for i in range(1,len(nums)):
            b[i]=nums[i-1]*b[i-1]
        for j in range(len(nums)-2,-1,-1):
            tmp*=nums[j+1]
            b[j]*=tmp

        return b


