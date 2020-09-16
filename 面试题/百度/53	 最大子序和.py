class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        Sum=0
        max_depth=nums[0]
        if max(nums)<0:
            return max(nums)
        for i in range(0,len(nums)):
            Sum+=nums[i]
            max_depth = max(max_depth,Sum)
            if Sum<0:
                Sum=0
        return max_depth