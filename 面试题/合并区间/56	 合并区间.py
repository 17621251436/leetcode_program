class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(keys=lambda  x:x[0])
        merge=[]
        for interval in intervals:
            if not merge or interval[0]>merge[-1][1]:
                merge.append(interval)
            else:
                merge[-1][1]=max(merge[-1][1],interval[1])
        return merge



