class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if max(nums) < 0:
            return max(nums)
        ans = 0
        max_sum = 0
        for num in nums:
            ans += num
            if ans < 0:
                ans = 0
            max_sum = max(max_sum, ans)
        return max_sum


