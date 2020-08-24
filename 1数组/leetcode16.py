#最接近的三数之和
#给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
# 找出 nums 中的三个整数，使得它们的和与 target 最接近。
# 返回这三个数的和。假定每组输入只存在唯一答案。
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10**7

        # 根据差值的绝对值来更新答案
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur

        # 枚举 a
        for i in range(n):
            # 保证和上一次枚举的元素不相等
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 使用双指针枚举 b 和 c
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                # 如果和为 target 直接返回答案
                if s == target:
                    return target
                update(s)
                if s > target:
                    # 如果和大于 target，移动 c 对应的指针
                    k = k - 1
                    # 移动到下一个不相等的元素
                    while j < k and nums[k] == nums[k+1]:
                        k = k - 1

                else:
                    # 如果和小于 target，移动 b 对应的指针
                    j= j + 1
                    # 移动到下一个不相等的元素
                    while j < k and nums[j] == nums[j-1]:
                        j+= 1


        return best

