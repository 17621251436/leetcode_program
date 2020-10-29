#找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

#说明：
#所有数字都是正整数。
#解集不能包含重复的组合。
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = list(range(1, 9))
        res = []

        def dfs(i,sunNum,arr):
            if sunNum==n and len(arr)==k:
                res.append(arr)
            if len(arr)==k:
                return
            for j in range(i,len(candidates)):
                dfs(j+1,sunNum+candidates[j],arr+[candidates[j]])
        dfs(0,[],[])
        return res









class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = list(range(1, 10))
        res = []

        def backtrack(i, temp_sum, temp_list):
            if temp_sum == n and len(temp_list) == k:
                res.append(temp_list)
                return

            if len(temp_list) == k:
                return

            for j in range(i, len(candidates)):
                if len(temp_list) == k - 1:
                    if temp_sum + candidates[j] > n or temp_sum + candidates[-1] < n:  # 稍微优化了一下
                        break
                backtrack(j + 1, temp_sum + candidates[j], temp_list + [candidates[j]])

        backtrack(0, 0, [])
        return res



