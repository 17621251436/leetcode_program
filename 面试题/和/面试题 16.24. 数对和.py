class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        res=[]
        nums.sort()
        p=0
        q=len(nums)-1
        while p<q:
            if nums[p]+nums[q]<target:
                p+=1
            elif nums[p]+nums[q]>target:
                q-=1
            else:
                res.append(nums[p],nums[q])
                p+=1
                q-=1
        return res




