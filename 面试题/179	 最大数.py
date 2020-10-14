class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if str(nums[j]) + str(nums[j + 1]) > str(nums[j + 1]) + str(nums[j]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        s = ''
        if nums[-1] == 0:
            return('0')
        for i in nums:
            s = str(i) + s
        return s



offer 59 数组组成最小数字
