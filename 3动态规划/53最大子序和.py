##
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        res=nums[0]
        for num in nums:
            sum+=num
            if sum >res:
                res=sum
            if sum<0:
                sum=0
        return res
