class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        num=sorted(nums)
        begin,end=0,0
        j=len(nums)-1
        for i in range(len(nums)):
            if num[i]!=nums[i]:
                begin=i
                break
        while j>=0:
            if nums[j]!=num[j]:
                end=j
                break
            j-=1
        if end==begin:
            return  0
        return end-begin+1