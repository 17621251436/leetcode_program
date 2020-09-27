class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums :
            return 0
        if max(nums)<0:
            return max(nums)
        Sum=0
        res=nums[0]
        for num in nums:
            Sum+=num
            if Sum<0:
                Sum=0
            res=max(res,Sum)
        return res

