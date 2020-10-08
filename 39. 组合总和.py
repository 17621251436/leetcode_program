class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
   
        if not candidates:
            return []
        res=[]
        def dfs(i,sumNum,path):
            if sumNum==target:
                res.append(path)
                return
            if sumNum>target:
                return
            for j in range(i,len(candidates)):
                dfs(j,sumNum+candidates[j],path+[candidates[j]])
        dfs(0,0,[])
        return res


# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         def dfs(candidates, begin, size, res, path, target):
#             if target < 0:
#                 return
#             if target == 0:
#                 res.append(path)
#                 return
#             for i in range(begin, size):
#                 dfs(candidates, i, size, res, path + [candidates[i]], target - candidates[i])
#
#         begin = 0
#         size = len(candidates)
#         res = []
#         path = []
#         if size == 0:
#             return []
#         dfs(candidates, 0, size, res, path, target)
#         return res
#
#
#
