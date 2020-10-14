class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True

        def dfs(nums):
            temp = nums[-1]
            for i in range(len(nums)):
                if nums[i] > temp:
                    break
            for j in range(i, len(nums)):
                if nums[j] < temp:
                    return False

            left = True
            if i > 0:
                left = dfs(nums[:i])
            right = True
            if i < len(nums) - 1:
                right = dfs(nums[i:-1])
            return left and right

        return dfs(postorder)

        # if not postorder:
        #     return True

        # def dfs(nums):
        #     if not nums:
        #         return True
        #     temp = nums[-1]
        #     for i in range(len(nums)):
        #         if nums[i] > temp:
        #             break
        #     for j in range(i, len(nums) - 1):
        #         if nums[j] < temp:
        #             return False
        #     left = True
        #     if i > 0:
        #         left = dfs(nums[:i])
        #     right = True
        #     if i < len(nums) - 1:
        #         right = dfs(nums[i:-1])
        #     return left and right

        # return dfs(postorder)