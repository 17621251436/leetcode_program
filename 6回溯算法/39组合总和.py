class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res=[]
        def back(i,sunNum,path):
            if sunNum==target:
                res.append(path)
                return
            if sunNum>target:
                return
            for j in range(i,len(candidates)):
                back(j,sunNum+candidates[j],path+[candidates[j]])
        dfs(0,0,[])
        return res











