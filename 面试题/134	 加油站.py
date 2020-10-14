class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        maxval = float('-inf')
        idx = -1
        # 求后缀和
        postsum = 0
        for i in range(n - 1, -1, -1):
            postsum += gas[i] - cost[i]
            if postsum > maxval:
                maxval = postsum
                idx = i
        return idx if postsum >= 0 else -1


