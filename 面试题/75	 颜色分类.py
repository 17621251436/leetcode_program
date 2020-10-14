#我们可以考虑对数组进行两次遍历。在第一次遍历中，我们将数组中所有的 00 交换到数组的头部。在第二次遍历中，我们将数组中所有的 11 交换到头部的 00 之后。此时，所有的 22 都出现在数组的尾部，这样我们就完成了排序。


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        ptr = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1

