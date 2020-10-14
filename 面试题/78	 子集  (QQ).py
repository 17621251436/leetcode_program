class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[], ]
        if not nums:
            return res

        for num in nums:
            res += [arr + [num] for arr in res]
        return res


