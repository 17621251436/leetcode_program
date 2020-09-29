class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res=[]
        def dfs(nums,path):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:],path+[nums[i]])
        dfs(nums,[])
        return res

##又重复数
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if not nums:
            return []
        res = []
        check=[0 for _ in range(lne(nums))]
        def dfs(nums, path，check):
            if len(nums)==len(path):
                res.append(path)
            for i in range(len(nums)):
                if check[i]==1:
                    continue
                if check[i-1] ==0 and i>0 and nums[i]==nums[i-1]:
                    continue
                check[i]=1
                dfs(nums, path + [nums[i]],check)
                check[i]=0

        dfs(nums, [],check)
        return res


