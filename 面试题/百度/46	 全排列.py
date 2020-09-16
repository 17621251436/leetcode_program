class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []

        def dfs(nums, tmp):
            if not nums:
                res.append(tmp)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        dfs(nums, [])
        return res