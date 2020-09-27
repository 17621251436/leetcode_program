class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp=sorted(nums)
        n =len(nums)
        p1=temp[:(n+1)//2][::-1]
        p2=temp[(n+1)//2:][::-1]
        nums[::2]=p1
        nums[1::2]=p2