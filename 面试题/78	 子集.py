class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[],]
        if not nums:
            return res
        for num in nums:
            res+=[[num]+i for i in res]
        return res

