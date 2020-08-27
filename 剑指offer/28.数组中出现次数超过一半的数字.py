class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        numbers.sort()
        lenth=len(numbers)
        if not numbers:
            return None
        for i in range(numbers):
            if numbers[i]==nums[i+lenth//2]:
                return numbers[i]

