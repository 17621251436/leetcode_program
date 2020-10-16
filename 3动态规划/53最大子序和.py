class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if max(nums)<0:
            return max(nums)
        Sum=0
        max_sum=0
        for num in nums:
            Sum+=num
            if Sum<0:
                Sum=0
            max_sum=max(max_sum,Sum)
        return max_sum

