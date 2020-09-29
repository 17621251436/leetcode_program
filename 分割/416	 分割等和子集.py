class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        @lru_cache
        def dfs(i, sum1, sum2):
            if sum1 == sum2: return True
            if sum2 > sum1 or i >= len(nums): return False
            return dfs(i + 1, sum1 - nums[i], sum2 + nums[i]) or dfs(i + 1, sum1, sum2)

        total = sum(nums)
        if total % 2 == 1: return False
        return dfs(0, total, 0)

