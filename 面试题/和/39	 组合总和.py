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

