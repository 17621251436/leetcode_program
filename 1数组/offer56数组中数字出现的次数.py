class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:

        i=1
        abmap={}
        tmp=[]
        for i in range(len(nums)):
            abmap[nums[i]]=abmap.get(nums[i],0)+1
            i+i+1

        for i ,v in abmap.items():
            if v==1:
                tmp.append(i)
        return tmp



